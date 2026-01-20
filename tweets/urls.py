from django.urls import path
from . import views

urlpatterns = [
    # Feed / Home
    path('', views.feed, name='feed'),

    # Tweet CRUD operations
    path('create/', views.create_tweet, name='create_tweet'),
    path('edit/<int:tweet_id>/', views.edit_tweet, name='edit_tweet'),
    path('delete/<int:tweet_id>/', views.delete_tweet, name='delete_tweet'),

    # Authentication
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
