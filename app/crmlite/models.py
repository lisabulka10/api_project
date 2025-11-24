from django.db import models


class Company(models.Model):
    INN = models.CharField(max_length=12, unique=True)
    title = models.CharField(max_length=256)


class Storage(models.Model):
    address = models.CharField()
    company_id = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='storage')
