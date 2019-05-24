from django.urls import path
from django.contrib.auth import views as auth_views

from gringo_tv.custom_profile import views, forms

app_name = 'customer'

urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(authentication_form=forms.LoginForm), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
]
