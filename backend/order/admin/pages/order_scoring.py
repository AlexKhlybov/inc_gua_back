from ...models import OrderScoringPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(OrderScoringPage)
class OrderScoringPageAdmin(BasePageAdmin):
    pass
