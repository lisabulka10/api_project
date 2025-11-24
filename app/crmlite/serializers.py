from rest_framework import serializers
from .models import Company, Storage


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['INN', 'title']


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['address', 'company_id']

