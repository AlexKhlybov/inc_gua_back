from django.contrib import admin
from ..models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'role', 'last_name', 'first_name', 'is_active')

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return (
                (None, {
                    'classes': ('wide',),
                    'fields': ('email', 'password1', 'password2',),
                }),)
        return (
            (None, {'fields': ('role', 'password')}),
            (_('Personal info'),
             {'fields': (
                 'last_name', 'first_name', 'patronymic', 'email', 'phone', 'authority', 'password_reset_key', 'logo'
             )}),
            (_('Permissions'), {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            }),
            (_('Important dates'), {'fields': ('last_login', 'date_joined')}),)
