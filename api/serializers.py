
from django.contrib.auth.models import User
import drf_writable_nested
from api.models import Address,Book,Author
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class AddressSerializer(serializers.ModelSerializer):
   class Meta:
       model = Address
       fields = ("detail", "city") 


class UserSerializer(serializers.ModelSerializer):
    
    addresses=AddressSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ("username", "email", "addresses")

class AuthorSerializer(serializers.ModelSerializer):
   class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
   
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields =  "__all__"
    # def create(self, validated_data):
    #     return Book.objects.create(**validated_data)

    # def get_author_set(self, object):
    #    return BookSerializer(object.author, many=True).data