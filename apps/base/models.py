
from django.db import models

from apps.accounts.models import Usuario
from apps.blog.models import Post

'''
class User(AbstractUser):
    pass

    def __str__(self):
        return self.username'''


class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de Modificación',auto_now = True, auto_now_add = False)
    fecha_eliminacion = models.DateField('Fecha de Eliminación',auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True



class Web(ModeloBase):
    nosotros = models.TextField('Nosotros')
    telefono = models.CharField('Teléfono', max_length=10)
    email = models.EmailField('Correo Electrónico', max_length=200)
    direccion = models.CharField('Dirección', max_length=200)

    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'

    def __str__(self):
        return self.nosotros


class RedesSociales(ModeloBase):
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.facebook


class Suscriptor(ModeloBase):
    correo = models.EmailField('Correo Electrónico', max_length=200)

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.correo


class Contacto(ModeloBase):
    name = models.CharField('Nombre', max_length=100, null=False, blank=False)
    email = models.EmailField('Email', blank=False, null=False)
    # telephone = models.CharField('Telefono', max_length=10, null=True)
    subject = models.CharField('Asunto', max_length=100, blank=False, null=True)
    message = models.CharField('Mensaje', max_length=110, blank=False, null=False)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = ' Contactos'

    def __str__(self):
        return self.subject
