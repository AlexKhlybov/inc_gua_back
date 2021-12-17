from ...models import PrincipalBindingsPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(PrincipalBindingsPage)
class PrincipalBindingsPageAdmin(BasePageAdmin):
    pass
