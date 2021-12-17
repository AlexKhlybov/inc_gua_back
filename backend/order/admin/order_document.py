from django.contrib import admin
from ..models import OrderDocument


@admin.register(OrderDocument)
class OrderDocumentAdmin(admin.ModelAdmin):
    pass
