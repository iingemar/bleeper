from __future__ import unicode_literals

from django.db import models
from django.urls import reverse_lazy

# Create your models here.

from app_name.models import Bleep


class HashTag(models.Model):
    tag = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag

    def get_bleeps(self):
        return Bleep.objects.filter(content__icontains='#' + self.tag)

    def get_absolute_url(self):
        return reverse_lazy('hashtags', kwargs={'hashtag': self.tag})
