from django.contrib import admin

from .models import Company, Storage


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['INN', 'title', 'owner']


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ['address', 'company']
