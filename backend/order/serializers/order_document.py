from rest_framework import serializers

from ..models import OrderDocument
from ..serializers.document_type import DocumentTypeSerializer
from ..serializers.order import OrderListSerializer


class OrderDocumentSerializer(serializers.ModelSerializer):
    order = OrderListSerializer(read_only=True)
    document_type = DocumentTypeSerializer(read_only=True)

    class Meta:
        model = OrderDocument
        fields = ['id', 'order', 'document', 'document_title', 'document_type', 'is_valid', 'create_at', 'update_at']


class OrderDocumentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDocument
        fields = ['id', 'order', 'document', 'document_title', 'document_type', 'is_valid', 'create_at', 'update_at']


class OrderDocumentCreateSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super(OrderDocumentCreateSerializer, self).to_representation(instance)
        data['order'] = OrderListSerializer(instance.order).data
        data['document_type'] = DocumentTypeSerializer(instance.document_type).data

        return data

    class Meta:
        model = OrderDocument
        fields = ['id', 'order', 'document', 'document_title', 'document_type', 'is_valid', 'create_at', 'update_at']
