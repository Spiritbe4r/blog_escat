from django.contrib.auth.decorators import login_required
from django.urls import path, include


from .views import (FormularioContacto,Suscribir)  # PostDetailView, PostCreateView, PostUpdateView, PostDeleteView)

# app_name = 'base'
urlpatterns = [

    
    path('contact/', FormularioContacto.as_view(), name='contact'),
    path('suscribirse/', Suscribir.as_view(), name='suscribirse'),
   # path('<slug:slug>/like/', PostLikeToggle.as_view(), name='like-toggle'), # new

    
   # path('accounts/', include('allauth.urls')),
    
    
    
]
