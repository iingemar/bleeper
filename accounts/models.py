from __future__ import unicode_literals

from django.conf import settings
from django.db import models

# Create your models here.


class UserProfileManager(models.Manager):
    def all(self):
        qs = self.get_queryset().all()
        try:
            if self.instance:
                qs = qs.exclude(user=self.instance)
        except:
            pass
        return qs

    def user_follow(self, user, toggle_user):
        # Returns tuple (user_profile, boolean created)
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if toggle_user in user_profile.following:
            user_profile.following.remove(toggle_user)
        else:
            user_profile.following.add(toggle_user)


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
