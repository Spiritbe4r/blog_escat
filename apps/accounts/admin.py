from django.contrib import admin
from django.contrib.auth import get_user_model
from apps.accounts.models import Usuario

# Register your models here.


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import UserAdminChangeForm, UserAdminCreationForm


@admin.register(Usuario)
class UserInAdmin(UserAdmin):
    """ All User Admin Model (Include Super User) """
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    search_fields = ['email', 'first_name', 'last_name', 'is_admin', 'is_active']
    list_display = ['email', 'is_admin', 'is_active','token']
    list_filter = ['is_admin', 'is_active']
    readonly_fields = ('created_at', 'updated_at', 'last_login','token')
    
    fieldsets = (
        (None, {'fields': ('username','email', 'password', ('first_name', 'last_name'),)}),
       # ('Contact', {
            # 'classes': ('collapse',),
       #     'fields': ('number', 'website',)
       # }),
        ('Biographical Details', {
            # 'classes': ('collapse',),
            'fields': ('avatar',)
        }),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
        # ('Group Permissions', {'fields': ('groups', 'user_permissions')}), if add permissions class
        ('Time', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            # 'classes': ('wide',),
            'fields': ('first_name', 'last_name','username', 'email', 'password1', 'password2')}
         ),
    )
    ordering = ('email',)
    filter_horizontal = ()