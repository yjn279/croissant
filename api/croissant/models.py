from pyexpat import model
from tkinter.tix import Tree
from django.contrib.auth import get_user_model
from django.db import models


class Layer(models.Model):
    title = models.CharField(max_length=64, blank=True, default='')
    description = models.TextField(blank=True, default='')
    owner = models.ForeignKey(get_user_model(), related_name='own', on_delete=models.CASCADE, default=0)  # 自身を自動で入れる
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
#     task = models.PositiveIntegerField(default=1)
#     layer = models.ForeignKey(Layer)
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
#     date = models.DateField()  # default today
#     time = models.TimeField()
#     created = models.DateTimeField(auto_now_add=True)


# class End(models.Model):
#     date = models.DateField()
#     time = models.TimeField()
#     created = models.DateTimeField(auto_now_add=True)
    