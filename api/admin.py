from django.contrib import admin
from api.models import Address,Author,Book

# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display=['id','user','detail','city']

admin.site.register((Author,Book))