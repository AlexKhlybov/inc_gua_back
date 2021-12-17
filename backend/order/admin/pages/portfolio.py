from ...models import PortfolioPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(PortfolioPage)
class PortfolioPageAdmin(BasePageAdmin):
    pass
