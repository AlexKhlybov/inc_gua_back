from rest_framework import serializers

from entity.models.legal_entity import LegalEntity
from entity.serializers.principal import PrincipalSerializer
from ..models.limit_principal import LimitPrincipalModel


class LimitPrincipalSerializer(serializers.ModelSerializer):

    class Meta:
        model = LegalEntity
        fields = ['inn', ]
        # fields = '__all__'


class LimitPrincipalUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = LimitPrincipalModel
        fields = ['principal', ]


class LimitPrincipalBaseSerializer(serializers.ModelSerializer):
    principal = PrincipalSerializer(read_only=True)

    class Meta:
        model = LimitPrincipalModel
        fields = '__all__'
