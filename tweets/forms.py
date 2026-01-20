from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tweet


class TweetForm(forms.ModelForm):
    """Form for creating and editing tweets"""

    class Meta:
        model = Tweet
        fields = ['text', 'image']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "What's happening?",
                'rows': 3,
                'maxlength': 280
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/jpeg,image/png,image/gif'
            })
        }
        labels = {
            'text': 'Tweet',
            'image': 'Image (optional)'
        }

    def clean_image(self):
        """Validate image file size (max 5MB)"""
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # 5MB
                raise forms.ValidationError('Image file size must be under 5MB')
        return image


class CustomUserCreationForm(UserCreationForm):
    """Custom user registration form with email field"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
