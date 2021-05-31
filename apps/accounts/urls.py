
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import (Login,logoutUsuario,ListadoUsuario,RegistrarUsuario,register_view,ResetPasswordView,ChangePasswordView)

# app_name = 'base'
urlpatterns = [
    
  #  path('accounts/', include('allauth.urls')),
    path('register/', register_view,name='register'),
    #path('signup/', register_view,name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', login_required(logoutUsuario), name='logout'),
    path('list_users/', login_required(ListadoUsuario.as_view()), name='list_users'),
    path('reset/password/', ResetPasswordView.as_view(), name='reset_password'),
    path('change/password/<str:token>/', ChangePasswordView.as_view(), name='change_password'),
    
    
    
    
]