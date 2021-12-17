from django.contrib import admin
from ..models import Lot


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    pass
