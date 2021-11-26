from django.contrib import admin
from .models import Message, Comment


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'user_from', 'user_to', 'created')
    list_filter = ('user_from', 'user_to', 'created')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text')
    list_filter = ('author',)
