import datetime
import random
from django.shortcuts import render

from django.template import RequestContext
from config.settings import EMAIL_HOST_USER
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import *
from django.core.mail import get_connection, send_mail
from django.db.models import Q
from django.http import HttpResponseRedirect, request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
# from django.views.generic import TemplateView
from django.views.generic.base import RedirectView, View
from django.views.generic.edit import FormView

from apps.base.models import Post
from apps.blog.models import Categoria, Like, Post

from .utils import consulta, generarCategoria, obtenerRedes, obtenerWeb

#errors
from django.http import HttpResponse


class Home(ListView):

    def get(self, request, *args, **kwargs):

        posts = list(Post.objects.filter(
            estado=True,
            publicado=True
        ).values_list('id', flat=True))
        principal = random.choice(posts)
        posts.remove(principal)
        principal = consulta(principal)
        user = request.user

        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)
        post4 = random.choice(posts)
        posts.remove(post4)

        week_ago = datetime.date.today() - datetime.timedelta(days=7)
        try:
            post_escatologia = Post.objects.filter(
                estado=True,
                publicado=True,
                categoria=Categoria.objects.get(nombre__iexact='Escatologia')
            ).latest('fecha_publicacion')
        except:
            post_escatologia = None

        try:
            post_todos = Post.objects.filter(
                estado=True,
                publicado=True,
                categoria=Categoria.objects.get(nombre__iexact='Todos')
            ).latest('fecha_publicacion')
        except:
            post_todos = None

        try:

            trends = Post.objects.filter(time_upload__gte=week_ago).order_by('-post_views')
        except:
            trends = None

        contexto = {
            'principal': principal,
            'post1': consulta(post1),
            'post2': consulta(post2),
            'post3': consulta(post3),
            'post4': consulta(post4),
            'user': user,
            'titulo': 'Blog',
            'subtitulo': 'Escatologico',
            'post_todos': post_todos,
            'post_escatologia': post_escatologia,
            'sociales': obtenerRedes(),
            'web': obtenerWeb(),
            'trends': trends,
            'pop_post': Post.objects.order_by('-post_views')[:9],
        }

        return render(request, 'index.html', contexto)


class Listado(ListView):

    def get(self, request, nombre_categoria, *args, **kwargs):
        contexto = generarCategoria(request, nombre_categoria)

        return render(request, 'categoria.html', contexto)


'''

class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('base:home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print("Alguien ingreso")
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self, request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
'''


# Create your views here.

def like_post(request):
    user = request.user
    # obj=get_object_or_404(Post,slug=slug)
    # url_=obj.get_absolute_url()
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        url_ = post_obj.get_absolute_url()

        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return redirect(url_)


class PostListView(ListView):
    model = Post
    template_name = 'blog.html'

    context_object_name = ('posts')

    # queryset = Post.objects.filter(estado=True)

    def get_queryset(self):
        return self.model.objects.filter(estado=True)

    def get(self, request, *args, **kwargs):
        query = request.GET.get("buscar")

        posts = self.get_queryset()

        if query:
            posts = Post.objects.filter(
                Q(titulo__icontains=query) |

                Q(descripcion__icontains=query)
            ).distinct()

        return render(request, self.template_name, {'posts': posts})


class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        print(slug)
        obj = get_object_or_404(Post, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_


def recursos(request):
    return render(request, 'recursos.html')




'''
def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            conta = Contacto(name=form.cleaned_data['name'], email=form.cleaned_data['email'], telephone=form.cleaned_data['telephone'],
                             subject=form.cleaned_data['subject'], message=form.cleaned_data['message'])
            cd = form.cleaned_data
            # assert False
            con = get_connection(
                'django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['flywithmee20@gmail.com'],
                connection=con
            )
            conta.save()
            #return HttpResponseRedirect('/contact?submitted=True')
            return redirect('home')
    else:
        form = ContactForm()

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'contact.html', {'form': form, 'submitted': submitted})'''


class DetallePost(DetailView):
    def get(self, request, slug, *args, **kwargs):
        try:
            post = Post.objects.get(slug=slug)

        except AttributeError:
            print('Post no Existe')
            post = None
        except Post.DoesNotExist:
            return HttpResponse('Exception: Data Not Found')
        except ViewDoesNotExist:
            print('The View does not exist in views.py')
        posts = list(Post.objects.filter(
            estado=True,
            publicado=True
        ).values_list('id', flat=True))
        posts.remove(post.id)
        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)
        post4 = random.choice(posts)
        posts.remove(post4)

        post.post_views += 1
        post.save()
        contexto = {
            'post': post,
            'sociales': obtenerRedes(),
            'web': obtenerWeb(),
            'post1': consulta(post1),
            'post2': consulta(post2),
            'post3': consulta(post3),
            'post4': consulta(post4),
            'pop_post': Post.objects.order_by('-post_views')[:9],
        }
        return render(request, 'post.html', contexto)


def handler404(request, exception):
    context = RequestContext(request)
    err_code = 404
    response = render(request,"pages/errors/404.html", {"code":err_code}, context)
    response.status_code = 404
    return response

def handler500(request):
    context = {}
    response = render(request, "pages/errors/500.html", context=context)
    response.status_code = 500
    return response
