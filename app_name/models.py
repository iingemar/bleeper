from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


class Bleep(models.Model):
    # AUTH_USER_MODEL if we want to substitute with a custom User model
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=140)
    # Automatically set the field to now every time the object is saved.
    # Note! This will cause the field to have editable=False and blank=True
    # and therefore not show up in the admin panel.
    updated = models.DateTimeField(auto_now=True)
    # Automatically set the field to now when the object is first created.
    # Note! This will cause the field to have editable=False and blank=True
    # and therefore not show up in the admin panel.
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    # Called automatically every time a model is saved
    # For the model, not specifically on the field.
    def clean(self, *args, **kwargs):
        content = self.content
        if content == 'abc':
            raise ValidationError('ValidationError! content cannot be abc')
        return super(Bleep, self).clean(*args, **kwargs)
