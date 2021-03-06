"""project_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from app_name.views import BleepListView
from hashtags.views import HashTagView
from .views import home


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BleepListView.as_view(), name='home'),
    url(r'^bleeps/', include('app_name.urls', namespace='bleeps')),
    url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtags'),
    url(r'^profiles/', include('accounts.urls', namespace='profiles')),
    url(r'^api/bleeps/', include('app_name.api.urls', namespace='bleeps-api')),
]
