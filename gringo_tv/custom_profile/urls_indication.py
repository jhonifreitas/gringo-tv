from django.urls import path

from gringo_tv.custom_profile import views

app_name = 'indication'

urlpatterns = [
    path('', views.IndicationListView.as_view(), name='list'),
    path('formulario/', views.IndicationCreateView.as_view(), name='create'),
    path('formulario/<int:pk>/', views.IndicationUpdateView.as_view(), name='update'),
    path('deletar/<int:pk>/', views.IndicationDeleteView.as_view(), name='delete'),

    path('status/<int:pk>/', views.IndicationStatusView.as_view(), name='status'),
]
