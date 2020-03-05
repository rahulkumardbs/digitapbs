from rest_framework import routers, serializers, viewsets
from company.models import BankList, Product


class BankSerializer(serializers.HyperlinkedModelSerializer):
    """Bank Serializer"""
    class Meta:
        model = BankList
        fields = ['id', 'bank_id', 'bank_name', 'username_text']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """Product Serializer"""
    class Meta:
        model = Product
        fields = ['id', 'product_id', 'product_name']