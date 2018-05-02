from django.db import models


class Posts(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=280, blank=True, default='')

    class Meta:
        ordering = ('created',)
