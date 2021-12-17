from ...models.pages import ChangePassword
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(ChangePassword)
class ChangePasswordAdmin(BasePageAdmin):
    pass
