from django.contrib import admin
from ..models import BlackListItem


@admin.register(BlackListItem)
class BlackListItemAdmin(admin.ModelAdmin):
    pass
