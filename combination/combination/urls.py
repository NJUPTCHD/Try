from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('welcome.urls',namespace = 'welcome')),
    url(r'^retailer/',include('retailer.urls',namespace = 'retailer')),
    url(r'^other/',include('other.urls',namespace = 'other')),
]
