from django.conf.urls import url

from .views import (
    UserDetailView,
)

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='detail'),
]
