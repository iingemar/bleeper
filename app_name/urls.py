from django.conf.urls import url
from .views import (
    BleepCreateView,
    BleepDeleteView,
    BleepUpdateView,
    bleep_create_view,
    bleep_detail_view,
    index_view
)

urlpatterns = [
    url(r'^$', index_view, name='index_view'),
    url(r'^create/$', BleepCreateView.as_view(), name='bleep_create_view'),
    url(r'^(?P<pk>[0-9]+)/$', bleep_detail_view, name='bleep_detail_view'),
    url(r'^(?P<pk>[0-9]+)/edit/$', BleepUpdateView.as_view(), name='bleep_update_view'),
    url(r'^(?P<pk>[0-9]+)/delete/$', BleepDeleteView.as_view(), name='bleep_delete_view'),
]
