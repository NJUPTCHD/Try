from django.conf.urls import url

from other import views

app_name = 'other'
urlpatterns = [
    url(r'^other/',views.other,name = 'other')
]