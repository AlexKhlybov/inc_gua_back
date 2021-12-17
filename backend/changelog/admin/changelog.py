from changelog.models import ChangeLog
from django.contrib import admin


@admin.register(ChangeLog)
class ChangeLogAdmin(admin.ModelAdmin):
    list_display = (
        "action_on_model",
        "content_type",
        "object_id",
        "user",
        "role",
        "name",
        "field",
        "oldvalue",
        "newvalue",
        "changed",
    )
    readonly_fields = (
        "action_on_model",
        "user",
        "role",
        "name",
        "field",
        "oldvalue",
        "newvalue",
        "changed",
    )
    list_filter = (
        "role",
        "action_on_model",
        "content_type",
        "object_id",
    )
