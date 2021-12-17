from ...models import PrincipalCoownersPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(PrincipalCoownersPage)
class PrincipalCoownersPageAdmin(BasePageAdmin):
    pass
