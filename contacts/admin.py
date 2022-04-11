from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
     list_filter = ( 'owner',)
     list_display = ('id', 'first_name', 'last_name','country_code', 'phone_number','contact_picture', 'is_favorite')

