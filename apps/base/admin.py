from django.contrib import admin


from .models import *

# Register your models here.



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





# Register your models here.


admin.site.register(Web,WebAdmin)
admin.site.register(RedesSociales,RedesSocialesAdmin)
admin.site.register(Suscriptor,SuscriptorAdmin)
admin.site.register(Contacto)

