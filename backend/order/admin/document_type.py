from django.contrib import admin
from ..models.document_type import DocumentType


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    pass
