
import os

from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.text import slugify
from apps.accounts.models import Usuario



class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    fecha_eliminacion = models.DateField('Fecha de Eliminación', auto_now=True, auto_now_add=False)

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


'''
class PublisshedManager(models.Manager):
    def get_queryset(self):
        return super(PublisshedManager, self).get_queryset().filter(status='published')'''


class Post(ModeloBase):
    # STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))

    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    titulo = models.CharField('Título del Post', max_length=150, unique=False)
    slug = models.SlugField('Slug', max_length=150, unique=True, null=True, blank=True)
    descripcion = models.TextField('Descripción', max_length=100, null=False, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    contenido = RichTextField()
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to='imagenes/', max_length=255)
    publicado = models.BooleanField('Publicado / No Publicado', default=False)
    fecha_publicacion = models.DateField('Fecha de Publicación')
    likes = models.ManyToManyField(Usuario, default=None, blank=True, related_name='post_likes')
    post_views = models.IntegerField(default=0, null=True, blank=True)

    # object = models.Manager()
    #  published = PublisshedManager()

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.imagen_referencial.path):
            os.remove(self.imagen_referencial.path)
            super(Post, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('base:detalle_post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = ' Comentarios'

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    LIKE_CHOICES = (('Like', 'Like'), ('Unlike', 'Unlike'),)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    '''def __str__(self):
        return self.user.username'''

    def __str__(self):
        return str(self.post)
