from django.conf.urls import url, include
# from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from client.models import Client, ClientProduct, ClientAddress


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    """Client Serializer"""
    class Meta:
        model = Client
        fields = ['id', 'username', 'name', 'phone']


class ClientProductSerializer(serializers.HyperlinkedModelSerializer):
    """Client Product Serializer"""
    class Meta:
        model = ClientProduct
        fields = ['id', 'client_id', 'product_id']
