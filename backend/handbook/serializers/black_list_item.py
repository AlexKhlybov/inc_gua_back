from rest_framework import serializers

from ..models import BlackListItem


class BlackListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackListItem
        fields = ['id', 'title', 'inn', 'comment', 'create_at', 'update_at']
