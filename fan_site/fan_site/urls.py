"""fan_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from app.views import home_view,bio_view, detail_view, region_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name="home_view"),
    url(r'^bio/$', bio_view, name="bio_view"),
    url(r'^details/$', detail_view, name="detail_view"),
    url(r'^region/(?P<region_id>\d+)/$', region_view, name="region_view")
]
