from django.contrib import admin
from ..models import Auction


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    pass
