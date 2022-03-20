from django.contrib.auth import get_user_model
from django.db import models


class Layer(models.Model):
    title = models.CharField(max_length=64, blank=True, default='')
    description = models.TextField(blank=True, default='')
    children = models.ManyToManyField('self', blank=True)
    tasks = models.PositiveIntegerField(default=1)
    progress = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(get_user_model(), related_name='own', on_delete=models.CASCADE)  # 自身を自動で入れる
    participants = models.ManyToManyField(get_user_model(), related_name='participate')  # デフォルトを自身に
    start_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_date = models.DateField(null=True)
    end_time = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_date']
