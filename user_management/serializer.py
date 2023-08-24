from django.contrib.auth import authenticate
from django.contrib.auth.hashers import *
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'password',
            'full_name',
            'roles',
            'phone_number'
        ]

        extra_kwargs = {
            'password': {'write_only': True}  # Ensure password is write-only
        }

        def create(self, validated_user_data):
            validated_user_data['password'] = make_password(validated_user_data['password'])
            user = User.objects.create_user(**validated_user_data)
            return user

