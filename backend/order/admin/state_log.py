from django.contrib import admin

from django_fsm_log.admin import StateLog


@admin.register(StateLog)
class StateLogAdmin(admin.ModelAdmin):
    pass
