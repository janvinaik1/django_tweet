from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Tweet(models.Model):
    """Model representing a tweet/post"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    text = models.TextField(max_length=280, help_text='Tweet content (max 280 characters)')
    image = models.ImageField(
        upload_to='tweet_images/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])],
        help_text='Optional image (JPG, PNG, GIF only)'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'

    def __str__(self):
        return f'{self.author.username}: {self.text[:50]}...' if len(self.text) > 50 else f'{self.author.username}: {self.text}'
