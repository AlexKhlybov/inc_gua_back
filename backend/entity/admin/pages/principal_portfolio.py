from ...models import PrincipalPortfolioPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(PrincipalPortfolioPage)
class PrincipalPortfolioPageAdmin(BasePageAdmin):
    pass
