from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
class PostResource(resources.ModelResource):
    class Meta:
        model = Post


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','estado','fecha_creacion')
    search_fields = ['nombre']


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellidos','email','descripcion','fecha_creacion')
    search_fields = ['nombre','apellidos','email']


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','publicado','categoria','autor','descripcion','estado','fecha_publicacion','likes')
    search_fields = ['titulo','autor']


class WebAdmin(admin.ModelAdmin):
    list_display = ('nosotros','email','direccion','telefono','estado','fecha_creacion')
    search_fields = ['email']


class RedesSocialesAdmin(admin.ModelAdmin):
    list_display = ('facebook','twitter','instagram','estado','fecha_creacion')
    search_fields = ['facebook']


class SuscriptorAdmin(admin.ModelAdmin):
    list_display = ('correo','estado','fecha_creacion')
    search_fields = ['correo']
'''
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','slug','autor','publish','estado')
    list_filter = ('estado','fecha_creacion','publish','autor')
    search_fields = ('titulo','contenido')
    prepopulated_fields = {'slug':('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'publish'
    ordering = ('estado','publish')'''

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('titulo','publicado','autor','descripcion','estado','fecha_publicacion')
    search_fields = ['titulo','autor']
    resource_class = PostResource

# Register your models here.
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post,PostAdmin)


admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)