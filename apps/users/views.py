from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from . import serializers


class RegisterView(CreateAPIView):
    serializer_class = serializers.RegisterSerializer


class UsernameValidateView(APIView):
    pass


class EmailValidateView(APIView):
    pass
