from django.contrib import admin
from ..models import Guaranty


@admin.register(Guaranty)
class GuarantyAdmin(admin.ModelAdmin):
    pass
