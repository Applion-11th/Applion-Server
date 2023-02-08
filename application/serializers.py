from cgi import FieldStorage
from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Application

class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

