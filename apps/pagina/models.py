from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
import os


# Create your models here.

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True


class Categoria(ModeloBase):
    nombre = models.CharField('Nombre de la Categoría', max_length=100, unique=True)
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to='categoria/')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre


class Autor(ModeloBase):
    nombre = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=120)
    email = models.EmailField('Correo Electrónico', max_length=200)
    descripcion = models.TextField('Descripción')
    imagen_referencial = models.ImageField('Imagen Referencial', null=True, blank=True, upload_to='autores/')
    web = models.URLField('Web', null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0},{1}'.format(self.apellidos, self.nombre)


class Post(ModeloBase):
    titulo = models.CharField('Título del Post', max_length=150, unique=True)
    slug = models.CharField('Slug', max_length=150, unique=True)
    descripcion = models.TextField('Descripción')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contenido = RichTextField()
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to='imagenes/', max_length=255)
    publicado = models.BooleanField('Publicado / No Publicado', default=False)
    fecha_publicacion = models.DateField('Fecha de Publicación')

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.imagen_referencial.path):
            os.remove(self.imagen_referencial.path)
            super(Post, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo


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


class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=100, null=False, blank=False)
    email = models.EmailField('Email', blank=False, null=False)
    subject = models.CharField('Telefono', max_length=20, blank=False, null=True)
    asunto = models.CharField('Asunto', max_length=100)
    message = models.CharField('Mensaje', max_length=110, blank=False, null=False)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = ' Contactos'

    def __str__(self):
        return self.asunto


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = ' Comentarios'

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
