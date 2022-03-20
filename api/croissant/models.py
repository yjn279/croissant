from django.contrib.auth import get_user_model
from django.db import models


class Layer(models.Model):
    title = models.CharField(max_length=64, blank=True, default='')
    description = models.TextField(blank=True, default='')
    owner = models.ForeignKey(get_user_model(), related_name='own', on_delete=models.CASCADE)  # 自身を自動で入れる
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


# class Progress(models.Model):
#     progress = models.PositiveIntegerField(default=0)
#     layer = models.ForeignKey(Layer)
#     created = models.DateTimeField(auto_now_add=True)


# class Task(models.Model):
#     layer_id = models.ForeignKey(Layer, related_name='tasks', on_delete=models.CASCADE)
#     task = models.PositiveIntegerField(default=1)
#     created = models.DateTimeField(auto_now_add=True)


# class Child(models.Model):
#     parent = models.ForeignKey(Layer)
#     child = models.ForeignKey(Layer)
#     created = models.DateTimeField(auto_now_add=True)


# class Participants(models.Model):
#     layer = models.ForeignKey(Layer)
#     user = models.ForeignKey(get_user_model())
#     created = models.DateTimeField(auto_now_add=True)


# class Start(models.Model):
#     layer_id = models.ForeignKey(Layer, related_name='start', on_delete=models.CASCADE)
#     date = models.DateField(blank=True, default='9999-99-99')
#     time = models.TimeField(blank=True, default='99:99')
#     created = models.DateTimeField(auto_now_add=True)


# class End(models.Model):
#     layer_id = models.ForeignKey(Layer, related_name='end', on_delete=models.CASCADE)
#     date = models.DateField(blank=True, default='9999-99-99')
#     time = models.TimeField(blank=True, default='99:99')
#     created = models.DateTimeField(auto_now_add=True)
    