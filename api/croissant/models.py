from django.contrib.auth import get_user_model
from django.db import models


class Layer(models.Model):
    title = models.CharField(max_length=64, blank=True)
    text = models.TextField(blank=True)
    layers = models.ManyToManyField('self', blank=True)
    participants = models.ManyToManyField(get_user_model(), related_name='participate')  # デフォルトを自身に
    creator = models.ForeignKey(get_user_model(), default=0, on_delete=models.CASCADE)  # 自身を自動で入れる
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
