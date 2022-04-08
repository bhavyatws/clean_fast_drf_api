from django.shortcuts import render
from api import serializers
from api.serializers import UserSerializer,AddressSerializer,BookSerializer
from rest_framework.generics import ListAPIView,ListCreateAPIView
from django.contrib.auth.models import User
from api.models import Book
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer

# Create your views here.
class UserList(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class BookListCreateAPIView(XLSXFileMixin,ListCreateAPIView):
    def get_queryset(self):
       queryset = Book.objects.all().select_related("author")
       return queryset
    serializer_class=BookSerializer
    renderer_classes = (XLSXRenderer,)
    filename = 'my_export.xlsx'
    
