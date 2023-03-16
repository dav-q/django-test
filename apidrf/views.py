from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import  check_password
from rest_framework import status
from .models import Client
import json

# Create your views here.


@api_view(['POST'])
def login(request):
    status_code=status.HTTP_401_UNAUTHORIZED
    response = {'status':'NotFound'}
    data = json.loads(request.body)
    client = Client.objects.filter(email=data['email']).first()
    if client:
        isAuth = check_password(data['password'], client.password)
        if isAuth:
            status_code=status.HTTP_200_OK
            response = {'status':'Success','auth':isAuth}

    return Response(response,status=status_code)
