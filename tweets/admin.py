from django.contrib import admin
from django.utils.html import format_html
from .models import Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    """Admin interface for Tweet model"""
    list_display = ['id', 'author', 'text_preview', 'has_image', 'created_at', 'updated_at']
    list_filter = ['created_at', 'author']
    search_fields = ['text', 'author__username']
    readonly_fields = ['created_at', 'updated_at', 'image_preview']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

    fieldsets = (
        ('Tweet Content', {
            'fields': ('author', 'text', 'image', 'image_preview')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def text_preview(self, obj):
        """Display first 50 characters of tweet text"""
        if len(obj.text) > 50:
            return f'{obj.text[:50]}...'
        return obj.text
    text_preview.short_description = 'Text'

    def has_image(self, obj):
        """Display whether tweet has an image"""
        if obj.image:
            return format_html('<span style="color: green;">✓</span>')
        return format_html('<span style="color: red;">✗</span>')
    has_image.short_description = 'Image'

    def image_preview(self, obj):
        """Display image preview in admin"""
        if obj.image:
            return format_html('<img src="{}" style="max-width: 300px; max-height: 300px;" />', obj.image.url)
        return 'No image'
    image_preview.short_description = 'Image Preview'
