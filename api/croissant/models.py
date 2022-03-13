from django.db import models


class Layer(models.Model):
    title = models.CharField(max_length=64, default='Untitled')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
