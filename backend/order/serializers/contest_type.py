from rest_framework import serializers

from ..models import ContestType


class ContestTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContestType
        fields = '__all__'
