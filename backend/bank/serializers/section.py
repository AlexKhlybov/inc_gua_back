from rest_framework import serializers
from ..models import Section
from bank.serializers.document import DocumentSerializer


class SectionSerializer(serializers.ModelSerializer):
    document = DocumentSerializer(read_only=True, many=True)

    class Meta:
        model = Section
        fields = ['id', 'document', 'title', 'create_at', 'update_at']
