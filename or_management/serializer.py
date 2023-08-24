from rest_framework import serializers
from .models import *


class OrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'product',
            'initializer',
            'agent',
            'selling_price',
            'buying_price',
            'profit',
            'status'
        ]


class OrderGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'product',
            'initializer',
            'agent',
            'selling_price',
            'buying_price',
            'profit',
            'status'
        ]
        depth = 2


class IncomeTransactionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeTransaction
        fields = [
            'order',
            'profit',
            'created_at'
        ]


class IncomeTransactionGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeTransaction
        fields = [
            'id',
            'order',
            'profit',
            'created_at'
        ]


class ClientPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'created_by',
            'order',
            'username',
            'phone'
        ]


class ClientGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'created_by',
            'order',
            'username',
            'phone'
        ]
        depth = 2
