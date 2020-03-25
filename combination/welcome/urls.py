from django.conf.urls import url
from django.urls import path, include
from welcome import views

app_name = 'welcome'
urlpatterns = [
    # url(r'^$',views.welcome,name = 'welcome'),
    path('',views.welcome,name = 'welcome'),
]