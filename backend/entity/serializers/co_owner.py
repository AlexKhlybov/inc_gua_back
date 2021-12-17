from rest_framework import serializers
from ..models.co_owner import CoOwner


class CoOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoOwner
        fields = ('id', 'title', 'create_at', 'update_at')
