from django.contrib import admin
from ..models import Person
from django.utils.translation import gettext_lazy as _


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic')

    def get_fieldsets(self, request, obj=None):
        return (
            (_('Personal info'),
             {'fields': ('last_name', 'first_name', 'patronymic', 'birth_date', 'birth_place', )}),
            (_('Passport info'), {
                'fields': ('passport_series', 'passport_number', 'department_code', 'collect_date', 'collect_by_whom',
                           'registration_address', 'citizenship',),
            }))
