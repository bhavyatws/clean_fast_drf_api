import imp
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Address(models.Model):
   detail = models.CharField(max_length=100)
   city = models.CharField(max_length=50)
   user = models.ForeignKey(User, related_name="addresses", on_delete=models.CASCADE)

class Author(models.Model):
   author_name = models.CharField(max_length=20)


class Book(models.Model):
   book_name = models.CharField(max_length=20)
   author = models.ForeignKey("Author", models.CASCADE, related_name="books")
   created_at = models.DateTimeField(auto_now_add=True)