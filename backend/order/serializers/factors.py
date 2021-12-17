from rest_framework import serializers

from ..models import Factors


class FactorsSerializer(serializers.ModelSerializer):
    catalog = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    def get_catalog(self, obj):
        return obj.get_catalog_display()

    def get_type(self, obj):
        return obj.get_catalog_display()

    class Meta:
        model = Factors
        fields = ('id', 'catalog', 'type', 'title', 'value')


class FactorsUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factors
        fields = ('__all__')
