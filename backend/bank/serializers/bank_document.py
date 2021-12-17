from rest_framework import serializers

from ..models import BankDocument
from bank.serializers.bank import BankSerializer
from order.serializers.document_type import DocumentTypeSerializer


class BankDocumentSerializer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True)
    document_type = DocumentTypeSerializer(read_only=True)

    document = serializers.SerializerMethodField()

    def get_document(self, obj):
        return obj.get_document_url

    def get_document_type(self, obj):
        return obj.get_document_type_display()

    class Meta:
        model = BankDocument
        fields = ['id', 'bank', 'document', 'document_title', 'document_type', 'create_at', 'update_at']
