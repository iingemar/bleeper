from django.conf.urls import url

from .views import (
    BleepCreateAPIView,
    BleepListAPIView
)

urlpatterns = [
    url(r'^$', BleepListAPIView.as_view(), name='list'),
    url(r'^create/$', BleepCreateAPIView.as_view(), name='create'),

]
