from django.contrib.auth import get_user_model
from django.db import models


class Layer(models.Model):
    title = models.CharField(max_length=64, blank=True, default='')
    description = models.TextField(blank=True, default='')
    # progress = models.  # 分母と分子に分ける？
    # complete = models.
    children = models.ManyToManyField('self', blank=True, default='')
    participants = models.ManyToManyField(get_user_model(), related_name='participate', blank=True)  # デフォルトを自身に
    owner = models.ForeignKey(get_user_model(), related_name='own', on_delete=models.CASCADE, default=0)  # 自身を自動で入れる
    start_date = models.DateField(blank=True, default='')
    start_time = models.TimeField(blank=True, default='')
    end_date = models.DateField(blank=True, default='')
    end_time = models.TimeField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_date']
