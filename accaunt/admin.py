from django.contrib import admin
from .models import AdvUser, Follower


@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    list_filter = ('username', 'first_name', 'last_name')
# Register your models here.


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('user_to', 'user_from', 'created')
    list_filter = ('user_to', 'user_from', 'created')
