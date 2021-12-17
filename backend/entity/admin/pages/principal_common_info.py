from ...models import PrincipalCommonInfoPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(PrincipalCommonInfoPage)
class PrincipalCommonInfoPageAdmin(BasePageAdmin):
    pass
