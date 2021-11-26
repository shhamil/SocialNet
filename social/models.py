from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from utils.default_user import User


class Message(models.Model):
    text = models.TextField(verbose_name='Текст сообщения')
    created = models.DateTimeField(auto_now_add=True)
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='От кого', related_name='user_from')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кому', related_name='user_to')


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор комментария', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_objects = GenericForeignKey('content_type', 'object_id')
    text = models.TextField(verbose_name='Текст сообщения')
