"""
Django admin customization
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),  # Bakal ada field permission di admin, yang isinya dibawah itu, nanti bisa dicentang
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),  # Bakal ada field important dates, yang isinya last login
    )
    readonly_fields = ['last_login',]  # Nggak bisa dimodifikasi, sisanya bisa
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # Buat assign custom css classes, kalau ga nanti tampilannya agak jelek (sunnah)
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
