from django.urls import path

from iptv.core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
]
