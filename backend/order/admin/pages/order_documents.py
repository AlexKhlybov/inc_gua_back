from ...models import OrderDocumentsPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(OrderDocumentsPage)
class OrderDocumentsPageAdmin(BasePageAdmin):
    pass
