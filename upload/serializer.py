from rest_framework import serializers
from .models import Documentform

class Meta:
        model = Document
        fields = ('description', 'document',) 