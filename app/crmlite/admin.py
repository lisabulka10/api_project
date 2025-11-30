from django.contrib import admin

from .models import Company, Storage
#, Supplier, Supply, Product


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['INN', 'title', 'owner']


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ['address', 'company']


# @admin.register(Supplier)
# class SupplierAdmin(admin.ModelAdmin):
#     list_display = ['company', 'title', 'INN']
#
#
# @admin.register(Supply)
# class SupplyAdmin(admin.ModelAdmin):
#     list_display = ['id', 'supplier', 'delivery_date']
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'purchase_price', 'sale_price', 'quantity', 'storage']
