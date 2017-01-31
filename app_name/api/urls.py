from django.conf.urls import url

from .views import (
    BleepListAPIView
)

urlpatterns = [
    url(r'^$', BleepListAPIView.as_view(), name='list'),

]
