from django import forms
from django.contrib.auth.forms import AuthenticationForm

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Your e-mail address', widget=forms.TextInput(attrs={'class': 'form-input'}))
    telephone = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-input'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-input'}))

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] ='form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre de usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'