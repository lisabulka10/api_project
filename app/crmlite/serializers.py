from rest_framework import serializers
from .models import Company, Storage


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['INN', 'title']


class StorageSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Storage
        fields = ['id', 'address', 'company']
        read_only_fields = ['company']
