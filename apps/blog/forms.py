
from apps.accounts.models import Usuario
from django import forms
from django.contrib.auth.forms import AuthenticationForm,get_user_model

from .models import Contacto
User=Usuario

'''
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Your e-mail address', widget=forms.TextInput(attrs={'class': 'form-input'}))
    telephone = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-input'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-input'}))'''

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] ='form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre de usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'


class FormContacto(forms.ModelForm):
    class Meta:
        model=Contacto
        fields='__all__'
        exclude=('estado',)

        widgets = {
            'name':forms.TextInput(
                attrs = {
                    'class':'form-input',
                    'placeholder':'Ingrese su nombre Completo',
                }
            ),
            
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-input',
                    'placeholder':'Ingrese su correo electrónico',
                }
            ),
            'subject':forms.TextInput(
                attrs = {
                    'class':'form-input',
                    'placeholder':'Ingrese el asunto',
                }
            ),
            'message':forms.Textarea(
                attrs = {
                    'class':'form-input',
                    'placeholder': 'Ingrese su mensaje',
                }
            ),

        }

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user       