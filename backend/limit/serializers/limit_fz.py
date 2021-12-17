from rest_framework import serializers

from ..models import LimitFZ


class LimitFZSerializer(serializers.ModelSerializer):

    class Meta:
        model = LimitFZ
        fields = ['id', 'fz', 'limit', 'create_at', 'update_at']
