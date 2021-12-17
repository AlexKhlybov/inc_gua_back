from django.contrib import admin
from ..models import GuarantyDocument


@admin.register(GuarantyDocument)
class GuarantyDocumentAdmin(admin.ModelAdmin):
    pass
