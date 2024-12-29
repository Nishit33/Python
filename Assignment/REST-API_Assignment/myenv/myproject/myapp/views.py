from django.shortcuts import render
from rest_framework import serializers
from rest_framework import generics
from .models import Book
from .serializers import Bookserializer

# Create your views here.


class Booklist(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer

class Bookupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer