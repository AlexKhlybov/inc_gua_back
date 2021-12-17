from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType

from ..models import ChangeLog
from user.serializers.user import UserSerializer


class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentType
        fields = "__all__"


class ChangeLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    content_type = ContentTypeSerializer(read_only=True)

    class Meta:
        model = ChangeLog
        fields = "__all__"
