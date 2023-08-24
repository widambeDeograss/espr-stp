
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import *
from rest_framework import serializers
from .models import Product ,Brand ,SubCategory ,Category




class BrandPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'name'
        ]
        
        
class BrandGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields =[
            'id', 'name'
        ]

        depth = 2  # this show hierarchical level of data return from request


class CategoryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "name"
        ]


class CateogoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name'
        ]
        depth = 1


class SubCategoryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = [
            'name', 'category'
        ]


class SubCategoryGetSerializer(serializers.ModelField):
    class Meta:
        model = SubCategory
        fields = [
            'id', 'name', 'category'
        ]
        depth = 2


class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name', 'buying_price', 'selling_price', 'brand', 'sub_category', 'image'
        ]


class ProductGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'buying_price', 'selling_price', 'brand', 'sub_category', 'image'
        ]

        depth = 2
