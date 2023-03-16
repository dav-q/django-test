from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import action,api_view
from django.contrib.auth.hashers import make_password, check_password
from .models import Client
import json


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id',
            'email',
            'name',
            'password',
            'created_at',
        )
        read_only_fields = ('created_at',)
    def create(self, data):
        data['password'] = make_password(data.get('password'))        
        user = Client.objects.create(**data)
        return user
    