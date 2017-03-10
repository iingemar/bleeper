from __future__ import unicode_literals
import re

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse

from .validators import validate_content


class BleepManager(models.Manager):
    def rebleep(self, user, parent_obj):
        if parent_obj.parent:
            original_parent = parent_obj.parent
        else:
            original_parent = parent_obj

        obj = self.model(
            parent = original_parent,
            user = user,
            content = parent_obj.content
        )
        obj.save()
        return obj


class Bleep(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    # AUTH_USER_MODEL if we want to substitute with a custom User model
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=140, validators=[
        validate_content
    ])
    # Automatically set the field to now every time the object is saved.
    # Note! This will cause the field to have editable=False and blank=True
    # and therefore not show up in the admin panel.
    updated = models.DateTimeField(auto_now=True)
    # Automatically set the field to now when the object is first created.
    # Note! This will cause the field to have editable=False and blank=True
    # and therefore not show up in the admin panel.
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = BleepManager()

    def __str__(self):
        return str(self.content)

    # Called automatically every time a model is saved
    # For the model, not specifically on the field.
    def clean(self, *args, **kwargs):
        content = self.content
        if content == 'abcd':
            raise ValidationError('Content cannot be abcd. /Bleep.clean')
        return super(Bleep, self).clean(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('bleeps:bleep_detail_view', kwargs={
            'pk': self.pk
        })

    class Meta:
        ordering = ['-timestamp']


# This is run every time a bleep object is saved.
def post_save_bleep_receiever(sender, instance, created, *args, **kwarags):
    print('post_save_bleep_receiever -------')
    print(instance)
    if created and not instance.parent:
        user_regexp = r'@(?P<username>[a-z_]+)'
        match = re.findall(user_regexp, instance.content)
        if match:
            print(match)
            # username = m.group('username')
            # print('username=' + username)

        hashtag_regexp = r'#(?P<hashtag>[\w\d-]+)'
        match = re.findall(hashtag_regexp, instance.content)
        if match:
            print(match)
            # hashtag = m.group('hashtag')
            # print('hashtag=' + hashtag)
    else:
        pass
    print('post_save_bleep_receiever -------')

post_save.connect(post_save_bleep_receiever, sender=Bleep)

