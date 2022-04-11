from rest_framework.serializers import ModelSerializer
from .models import Contact
from django.contrib.auth.admin import User


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact

        fields = ['id','country_code', 'first_name', 'last_name', 'phone_number','contact_picture', 'is_favorite']

def create(self, validated_data):
        user = Contact.objects.create_user(**validated_data)
        # Token.objects.create(user=user)
        return user