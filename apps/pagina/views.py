import random
from django.contrib.auth import login, logout
from django.core.mail import send_mail, get_connection
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from apps.pagina.forms import *
from .models import *
from .utils import consulta, obtenerRedes, obtenerWeb


class Home(ListView):

    def get(self, request, *args, **kwargs):
        posts = list(Post.objects.filter(
            estado=True,
            publicado=True
        ).values_list('id', flat=True))
        principal = random.choice(posts)
        posts.remove(principal)
        principal = consulta(principal)

        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)
        post4 = random.choice(posts)
        posts.remove(post4)

        try:
            post_escatologia = Post.objects.filter(
                                estado = True,
                                publicado = True,
                                categoria = Categoria.objects.get(nombre__iexact = 'Escatologia')
                                ).latest('fecha_publicacion')
        except:
            post_escatologia = None

        try:
            post_general = Post.objects.filter(
                            estado = True,
                            publicado = True,
                            categoria = Categoria.objects.get(nombre__iexact = 'Todos')
                            ).latest('fecha_publicacion')

        except:
            post_general = None

        contexto = {
            'principal': principal,
            'post1': consulta(post1),
            'post2': consulta(post2),
            'post3': consulta(post3),
            'post4': consulta(post4),
            'titulo':'Blog',
            'subtitulo':'Escatologico',
            'post_general': post_general,
            'post_escatologia': post_escatologia,
            'sociales': obtenerRedes(),
            'web': obtenerWeb(),
        }

        return render(request, 'home.html', contexto)


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

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


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = ('posts')
    queryset = Post.objects.filter(estado=True)


def detallePost(request, slug):

    post=get_object_or_404(Post,slug=slug)
    return render(request, 'home.html', {'detalle_post': post})


def recursos(request):
    return render(request, 'recursos.html')


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            conta = Contacto(name=form.cleaned_data['name'], email=form.cleaned_data['email'],
                             subject=form.cleaned_data['subject'], message=form.cleaned_data['message'])
            cd = form.cleaned_data
            # assert False
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['flywithmee20@gmail.com'],
                connection=con
            )
            conta.save()
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'contact.html', {'form': form, 'submitted': submitted})


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post


class PostDeleteView(DeleteView):
    model = Post
