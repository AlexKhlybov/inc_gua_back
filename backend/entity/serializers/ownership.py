from rest_framework import serializers

from ..models.ownership import Ownership
from .co_owner import CoOwnerSerializer
from .principal import PrincipalSerializer


class OwnershipSerializer(serializers.ModelSerializer):
    principal = CoOwnerSerializer(read_only=True)
    co_owner = PrincipalSerializer(read_only=True)

    class Meta:
        model = Ownership
        fields = ('id', 'title', 'principal', 'co_owner', 'fraction', 'create_at', 'update_at')
