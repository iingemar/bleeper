from django.conf.urls import url

from .views import (
    UserDetailView,
    UserFollowView
)

urlpatterns = [
    url(r'^(?P<username>[a-z_]+)/$', UserDetailView.as_view(), name='detail'),
    url(r'^(?P<username>[a-z_]+)/follow/$', UserFollowView.as_view(), name='follow'),
]
