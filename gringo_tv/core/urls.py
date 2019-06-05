from django.urls import path

from gringo_tv.core import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('configuracao/', views.ConfigView.as_view(), name='config'),
    path('configuracao/imagem/deletar', views.ConfigImageDeleteView.as_view(), name='delete-image-config'),
]
