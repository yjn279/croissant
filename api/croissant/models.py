from django.db import models


class Layer(models.Model):
    title = models.CharField(max_length=64, blank=True)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
