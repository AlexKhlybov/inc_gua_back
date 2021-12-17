from rest_framework import serializers

from ..models import OrderSpecialCondition


class OrderSpecialConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderSpecialCondition
        fields = ['id', 'title', 'description', 'create_at', 'update_at']
