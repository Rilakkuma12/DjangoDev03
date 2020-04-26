from django.shortcuts import render
from rest_framework.generics import CreateAPIView
# Create your views here.
from . import serializers


class RegisterView(CreateAPIView):
    serializer_class = serializers.RegisterSerializer



