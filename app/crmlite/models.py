from django.db import models


class Company(models.Model):
    INN = models.CharField(max_length=12, unique=True)
    title = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Storage(models.Model):
    address = models.CharField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='storage')

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
