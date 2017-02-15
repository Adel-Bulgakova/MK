from django.contrib import admin
from .models import Post


class Post_thumb(admin.ModelAdmin):
    list_display = ('thumbnail_image','title', 'published_date', 'is_published')

admin.site.register(Post, Post_thumb)