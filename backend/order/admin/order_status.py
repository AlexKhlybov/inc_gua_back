from django.contrib import admin
from ..models import OrderStatus


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    pass
