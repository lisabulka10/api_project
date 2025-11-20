from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from .models import Company, Storage

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()

    http_method_names = ["get", "delete", "post", "put"]


