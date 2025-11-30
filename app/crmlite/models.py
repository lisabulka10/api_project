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


# class Supplier(models.Model):
#     title = models.CharField()
#     INN = models.CharField()
#     company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='supplier')
#
#     class Meta:
#         verbose_name = 'Поставщик'
#         verbose_name_plural = 'Поставщики'
#
#
# class Supply(models.Model):
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supply')
#     delivery_date = models.DateTimeField()
#     products = models.ManyToManyField('Product', through='SupplyProduct', related_name='supplies')
#
#     class Meta:
#         verbose_name = 'Поставка'
#         verbose_name_plural = 'Поставки'
#
#
# class Product(models.Model):
#     title = models.CharField()
#     purchase_price = models.FloatField()
#     sale_price = models.FloatField()
#     quantity = models.PositiveIntegerField(default=0)
#     storage = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name='product')
#
#     class Meta:
#         verbose_name = 'Товар'
#         verbose_name_plural = 'Товары'
#
#
# class SupplyProduct(models.Model):
#     supply = models.ForeignKey(Supply, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#
#     class Meta:
#         verbose_name = 'ПоставкаТовар'
