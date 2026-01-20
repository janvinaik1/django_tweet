from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from .models import Tweet
from .forms import TweetForm, CustomUserCreationForm


def feed(request):
    """Display all tweets with pagination"""
    tweets_list = Tweet.objects.select_related('author').all()
    paginator = Paginator(tweets_list, 10)  # Show 10 tweets per page

    page_number = request.GET.get('page')
    tweets = paginator.get_page(page_number)

    return render(request, 'tweets/feed.html', {'tweets': tweets})


@login_required
def create_tweet(request):
    """Create a new tweet (authenticated users only)"""
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.author = request.user
            tweet.save()
            messages.success(request, 'Tweet posted successfully!')
            return redirect('feed')
    else:
        form = TweetForm()

    return render(request, 'tweets/create_tweet.html', {'form': form})


@login_required
def edit_tweet(request, tweet_id):
    """Edit an existing tweet (author only)"""
    tweet = get_object_or_404(Tweet, id=tweet_id)

    # Check if the user is the author
    if tweet.author != request.user:
        messages.error(request, 'You can only edit your own tweets.')
        return HttpResponseForbidden("You don't have permission to edit this tweet.")

    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tweet updated successfully!')
            return redirect('feed')
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweets/edit_tweet.html', {'form': form, 'tweet': tweet})


@login_required
def delete_tweet(request, tweet_id):
    """Delete a tweet (author only)"""
    tweet = get_object_or_404(Tweet, id=tweet_id)

    # Check if the user is the author
    if tweet.author != request.user:
        messages.error(request, 'You can only delete your own tweets.')
        return HttpResponseForbidden("You don't have permission to delete this tweet.")

    if request.method == 'POST':
        tweet.delete()
        messages.success(request, 'Tweet deleted successfully!')
        return redirect('feed')

    return render(request, 'tweets/delete_tweet.html', {'tweet': tweet})


def user_login(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('feed')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('feed')
    else:
        form = AuthenticationForm()

    return render(request, 'tweets/login.html', {'form': form})


def user_register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('feed')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after registration
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome, {user.username}!')
            return redirect('feed')
    else:
        form = CustomUserCreationForm()

    return render(request, 'tweets/register.html', {'form': form})


@login_required
def user_logout(request):
    """User logout view"""
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('feed')
