from ...models import OrderUnderwritingPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(OrderUnderwritingPage)
class OrderUnderwritingPageAdmin(BasePageAdmin):
    pass
