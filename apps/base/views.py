from django.core.mail import send_mail
from django.shortcuts import redirect, render
# from django.views.generic import TemplateView
from django.views.generic.base import View

from .models import Suscriptor
from config.settings import EMAIL_HOST_USER
from .forms import FormContacto
from apps.blog.utils import obtenerRedes, obtenerWeb


# from django.shortcuts import get_object_or_404
#from apps.base.forms import *


class FormularioContacto(View):
    def get(self,request,*args,**kwargs):
        form = FormContacto()
        contexto = {
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'form':form,
        }
        return render(request,'contact.html',contexto)

    def post(self,request,*args,**kwargs):
        form = FormContacto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:home')
        else:
            contexto = {
                'form':form,
            }
            return render(request,'contact.html',contexto)


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


class Suscribir(View):
    def post(self,request,*args,**kwargs):
        correo = request.POST.get('correo')
        Suscriptor.objects.create(correo = correo)
        asunto = 'GRACIAS POR SUSCRIBIRTE Al BLOG!'
        mensaje = 'Te has suscrito exitosamente al Blog, Gracias por tu preferencia!!!'
        try:
            send_mail(asunto,mensaje,EMAIL_HOST_USER,[correo])
        except:
            pass

        return redirect('base:home')

