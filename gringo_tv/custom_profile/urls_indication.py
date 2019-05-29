from django.urls import path
from django.contrib.auth import views as auth_views

from gringo_tv.custom_profile import views, forms

app_name = 'indication'

urlpatterns = [
    path('', views.IndicationListView.as_view(), name='list'),
    path('formulario/', views.IndicationCreateView.as_view(), name='create'),
    path('formulario/<int:pk>/', views.IndicationUpdateView.as_view(), name='update'),
    path('<int:pk>/', views.IndicationDeleteView.as_view(), name='delete'),
]
