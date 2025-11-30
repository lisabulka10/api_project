from rest_framework import serializers
from .models import Company, Storage
    # , Supplier, Supply, Product


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


# class SupplierSerializer(serializers.ModelSerializer):
#     company = CompanySerializer(read_only=True)
#
#     class Meta:
#         model = Supplier
#         fields = ['id', 'company', 'title', 'INN']
#         read_only_fields = ['company']
#
#
# class SupplySerializer(serializers.Serializer):
#     supplier = SupplierSerializer()
#
#     class Meta:
#         model = Supply
#         fields = ['supplier', 'delivery_date']
#
#
# class ProductSerializer(serializers.ModelSerializer):
#     storage = StorageSerializer()
#
#     class Meta:
#         model = Product
#         fields = ['id', 'title', 'purchase_price', 'sale_price', 'quantity', 'storage']
#         only_read_fields = ['quantity', 'storage']
