from ...models import PrincipalDocumentsPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(PrincipalDocumentsPage)
class PrincipalDocumentsPageAdmin(BasePageAdmin):
    pass
