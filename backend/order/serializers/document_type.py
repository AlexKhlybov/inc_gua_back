from rest_framework import serializers
from ..models.document_type import DocumentType


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ['id', 'type', 'title', 'create_at', 'update_at']
