from django.contrib import admin
from ..models import Principal


@admin.register(Principal)
class PrincipalAdmin(admin.ModelAdmin):
    list_display = ('title', 'legal_entity', )
