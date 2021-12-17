from ...models import OrderFinancialReportPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(OrderFinancialReportPage)
class OrderFinancialReportPageAdmin(BasePageAdmin):
    pass
