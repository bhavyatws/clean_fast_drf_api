from django.shortcuts import render
from api import serializers
from api.serializers import UserSerializer,AddressSerializer,BookSerializer
from rest_framework.generics import ListAPIView,ListCreateAPIView
from django.contrib.auth.models import User
from api.models import Book

# Create your views here.
class UserList(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class BookListCreateAPIView(ListCreateAPIView):
    def get_queryset(self):
       queryset = Book.objects.select_related("author").all()
       return queryset
    serializer_class=BookSerializer
    
