from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import (
    BleepCreateView,
    BleepDeleteView,
    BleepListView,
    BleepUpdateView,
    RebleepView,
    bleep_create_view,
    bleep_detail_view,
    index_view
)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/')),
    url(r'^search/$', BleepListView.as_view(), name='search_view'),
    url(r'^create/$', BleepCreateView.as_view(), name='bleep_create_view'),
    url(r'^(?P<pk>[0-9]+)/$', bleep_detail_view, name='bleep_detail_view'),
    url(r'^(?P<pk>[0-9]+)/rebleep/$', RebleepView.as_view(), name='rebleep_view'),
    url(r'^(?P<pk>[0-9]+)/edit/$', BleepUpdateView.as_view(), name='bleep_update_view'),
    url(r'^(?P<pk>[0-9]+)/delete/$', BleepDeleteView.as_view(), name='bleep_delete_view'),
]
