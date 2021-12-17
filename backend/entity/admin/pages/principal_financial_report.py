from ...models import PrincipalFinancialReportPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(PrincipalFinancialReportPage)
class PrincipalFinancialReportPageAdmin(BasePageAdmin):
    pass
