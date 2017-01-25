from django.conf.urls import url
from .views import (
    BleepCreateView,
    bleep_create_view,
    bleep_detail_view,
    index_view
)

urlpatterns = [
    url(r'^$', index_view, name='index_view'),
    url(r'^create/$', bleep_create_view, name='bleep_create_view'),
    url(r'^(?P<bleep_id>[0-9]+)$', bleep_detail_view, name='bleep_detail_view'),
]
