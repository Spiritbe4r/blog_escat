from django.contrib.auth.decorators import login_required
from django.urls import path, include

from aplicaciones.base.views import (Home, recursos, contact, Login, logoutUsuario, PostListView,
                                     DetallePost, Listado,
                                     Suscribir)  # PostDetailView, PostCreateView, PostUpdateView, PostDeleteView)

# app_name = 'base'
urlpatterns = [
    path('', (Home.as_view()), name='home'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('estudios_biblicos/', Listado.as_view(), {'nombre_categoria': 'ESTUDIOS BIBLICOS'}, name='estudios_biblicos'),
    path('devocionales/', Listado.as_view(), {'nombre_categoria': 'DEVOCIONALES'}, name='devocionales'),
    path('historia/', Listado.as_view(), {'nombre_categoria': 'HISTORIA'}, name='historia'),
    path('apologetica/', Listado.as_view(), {'nombre_categoria': 'APOLOGETICA'}, name='apologetica'),
    path('noticias/', Listado.as_view(), {'nombre_categoria': 'NOTICIAS'}, name='noticias'),
    path('evangelio/', Listado.as_view(), {'nombre_categoria': 'EVANGELIO'}, name='evangelio'),
    path('escatologia/', Listado.as_view(), {'nombre_categoria': 'ESCATOLOGIA'}, name='escatologia'),
    path('todos/', Listado.as_view(), {'nombre_categoria': 'TODOS'}, name='todos'),

    path('contact/', contact, name='contact'),
    path('suscribirse/', Suscribir.as_view(), name='suscribirse'),
    path('recursos/', recursos, name='recursos'),
    path('<slug:slug>/', DetallePost.as_view(), name='detalle_post'),
    path('accounts/', include('allauth.urls')),
    path('<slug:slug>/', DetallePost.as_view(), name='detalle_post'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/', login_required(logoutUsuario), name='logout'),
    # '''  path('<slug>/',PostDetailView.as_view(), name='detail'),
    #   path('<slug>/update/',PostUpdateView.as_view(), name='update'),
    #  path('<slug>/delete/',PostDeleteView.as_view(), name='delete'),
    #  path('create/',PostCreateView.as_view(), name='create'),'''
]
