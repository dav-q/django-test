from .models import Client
from rest_framework import viewsets,permissions
from .serializers import ClientSerializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import action,api_view
from django.contrib.auth.hashers import make_password, check_password
from .models import Client
from rest_framework import status

import json

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientSerializer

    @action(detail=False, methods=['get'])
    def ping(self, request, *args, **kwargs):
        response = {'pong':'true'}
        return Response(response,status=status.HTTP_201_CREATED)


