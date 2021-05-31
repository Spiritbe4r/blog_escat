import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.db import models
from django.contrib.auth.models import BaseUserManager

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,first_name,password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')

        user=self.model(
            username=username,
            email=self.normalize_email(email),
            first_name = first_name,
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username,email,first_name,password):
        user=self.create_user(
            email,
            username=username,
            first_name=first_name,
            password=password
        )
        user.is_admin=True
        user.save()
        return user




class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    # Names
    username = models.CharField('Nombre de usuario', max_length=100,unique=True)
    first_name = models.CharField('Nombres', max_length=200,blank=True ,null=True)
    last_name = models.CharField('Apellidos', max_length=200,blank=True ,null=True)
    # contact
    email = models.EmailField('Correo', max_length=254, unique=True)
    # about
    avatar = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=200, blank=True,null=True)
     # Permission
    is_active  = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # Registration
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #change password
    token = models.UUIDField(primary_key=False, default=uuid.uuid4,editable=False, null=True, blank=True)
    
    objects=UsuarioManager()
    # Main Field for authentication
    USERNAME_FIELD='username'
    # When user create must need to fill this field
    REQUIRED_FIELDS=['email','first_name']

    
    def __str__(self):
        return self.username  #or email 

    class Meta:
        ordering = ('-created_at', '-updated_at', )

    def get_full_name(self):
        if self.first_name:
            return f'{self.first_name}  {self.last_name}'
        return self.email.split('@')[0]

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin


'''
class User(AbstractBaseUser):
    """
    Custom abstract user Model.
    """
    # Names
    first_name = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True, unique=True)
    # contact
    email = models.EmailField(unique=True)  # require
    number = models.PositiveIntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    # about
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    # Registration
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Permission
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    # Main Field for authentication
    USERNAME_FIELD = 'username'
    # When user create must need to fill this field
    REQUIRED_FIELDS = ["email"]
    objects = UserManager()
    def __str__(self):
        return self.email
    class Meta:
        ordering = ('-created_at', '-updated_at', )
    def get_full_name(self):
        if self.first_name:
            return f'{self.first_name}  {self.last_name}'
        return self.email.split('@')[0]
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True


class UserManager(BaseUserManager):
    """ User Model Manager """
    def create_user(self,username, email, password=None, is_staff=False, is_admin=False, is_active=True,is_superuser=False):
        if not email:
            raise ValueError('Users must have email Address')
        if not password:
            raise ValueError('User must have Password')
        # if not full_name:
        #     raise ValueError('User must have a full name')
         
        user_obj = self.model(
            email=self.normalize_email(email),
            user = self.model(email=email, username=username)
        )
        
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.is_superuser=is_superuser
        user_obj.save(using=self._db)
    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user
    def create_superuser(self,name, email, password=None):
        user = self.create_user(
            name,
            email,
            password=password,
            is_staff=True,
            is_admin=True,
            is_superuser=True
            
        )
        return user'''