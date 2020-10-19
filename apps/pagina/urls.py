
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from apps.pagina.views import (Home, recursos, contact, Login, logoutUsuario, PostListView,
                               detallePost)  # PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, detallePost)

# app_name = 'pagina'
urlpatterns = [
    path('', login_required(Home.as_view()), name='home'),
    path('recursos/', recursos, name='recursos'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('contact/', contact, name='contact'),
    path('accounts/', include('allauth.urls')),
    path('<slug:slug>/', detallePost, name='detalle_post'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/', login_required(logoutUsuario), name='logout'),
    # '''  path('<slug>/',PostDetailView.as_view(), name='detail'),
    #   path('<slug>/update/',PostUpdateView.as_view(), name='update'),
    #  path('<slug>/delete/',PostDeleteView.as_view(), name='delete'),
    #  path('create/',PostCreateView.as_view(), name='create'),'''
]
