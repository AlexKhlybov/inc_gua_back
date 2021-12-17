from django.contrib import admin
from limit.models import LimitFZ


@admin.register(LimitFZ)
class LimitFZAdmin(admin.ModelAdmin):
    pass
