from ...models import PrincipalLimitPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(PrincipalLimitPage)
class PrincipalLimitPageAdmin(BasePageAdmin):
    pass
