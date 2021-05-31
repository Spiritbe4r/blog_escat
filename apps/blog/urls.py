from django.urls import path


from .views import ( PostListView, DetallePost, Listado,like_post)
app_name = 'blog'
urlpatterns = [
    
    path('posts/', PostListView.as_view(), name='blog'),
    path('estudios_biblicos/', Listado.as_view(), {'nombre_categoria': 'ESTUDIOS BIBLICOS'}, name='estudios_biblicos'),
    path('devocionales/', Listado.as_view(), {'nombre_categoria': 'DEVOCIONALES'}, name='devocionales'),
    path('historia/', Listado.as_view(), {'nombre_categoria': 'HISTORIA'}, name='historia'),
    path('apologetica/', Listado.as_view(), {'nombre_categoria': 'APOLOGETICA'}, name='apologetica'),
    path('noticias/', Listado.as_view(), {'nombre_categoria': 'NOTICIAS'}, name='noticias'),
    path('evangelio/', Listado.as_view(), {'nombre_categoria': 'EVANGELIO'}, name='evangelio'),
    path('escatologia/', Listado.as_view(), {'nombre_categoria': 'ESCATOLOGIA'}, name='escatologia'),
    path('todos/', Listado.as_view(), {'nombre_categoria': 'TODOS'}, name='todos'),
    
   # path('<slug:slug>/like/', PostLikeToggle.as_view(), name='like-toggle'), # new
    path('like/',like_post,name='like-post'),
    
   # path('accounts/', include('allauth.urls')),
    
    
    path('<slug:slug>/',DetallePost.as_view(), name = 'detalle_post'),
    path('', DetallePost.as_view(), name='detalle_post'),
    #path('<int:year>/<int:month>/<int', post.as_view(), name='detalle_post'),
]
handler404 = 'apps.blog.views.handler404'
handler500 = 'apps.blog.views.handler500'