from django.db import models
from django.contrib.auth.models import AbstractUser
from .services import get_unical_name


class AdvUser(AbstractUser):
    class Meta:
        db_table = 'AdvUser'

    about_me = models.CharField(blank=True, verbose_name='О себе', max_length=255)
    avatar = models.ImageField(blank=True, verbose_name='Аватарка', upload_to=get_unical_name)
    registrations_data = models.DateTimeField(auto_now_add=True)
    following = models.ManyToManyField('self', through='Follower', related_name='followers', symmetrical=False)


class Follower(models.Model):
    user_from = models.ForeignKey(AdvUser, related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey(AdvUser, related_name="rel_to_set", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


class Post(models.Model):
    author = models.ForeignKey(AdvUser, verbose_name='Автор поста', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    text = models.TextField(verbose_name='Текст поста')
    created = models.DateTimeField(auto_now_add=True)
