from ...models import PrincipalRatePage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(PrincipalRatePage)
class PrincipalRatePageAdmin(BasePageAdmin):
    pass
