from rest_framework import serializers

from entity.models.principal import Principal


class KonturPrincipalSerializer(serializers.ModelSerializer):
    inn = serializers.CharField()

    class Meta:
        model = Principal
        fields = ['inn']
