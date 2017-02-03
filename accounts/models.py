from __future__ import unicode_literals

from django.conf import settings
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    # One user has one profile
    # Accessed by user object.profile
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')

    # We can follow a lot of users and a lot of users can follow us.
    # user.profile.following -- users I follow
    # related_name is the reverse relationship: user.followed_by -- users that follow me
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')

    def __str__(self):
        return self.user.username + ' (' + str(self.following.all().count()) + ')'
