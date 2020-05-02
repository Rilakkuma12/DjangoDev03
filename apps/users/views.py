from django.shortcuts import render
from rest_framework.generics import CreateAPIView
# Create your views here.
<<<<<<< HEAD
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

=======
>>>>>>> origin/master
from . import serializers


class RegisterView(CreateAPIView):
    serializer_class = serializers.RegisterSerializer


<<<<<<< HEAD
class UsernameValidateView(APIView):
    pass


class EmailValidateView(APIView):
    pass
=======

>>>>>>> origin/master
