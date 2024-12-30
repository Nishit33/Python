from django.shortcuts import render
from rest_framework import serializers
from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.

class Userlist(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

class Userupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
