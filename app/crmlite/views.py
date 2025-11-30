from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.exceptions import ValidationError, NotFound

from rest_framework.permissions import IsAuthenticated

# from drf_spectacular.utils import extend_schema
# from .schemas import storage_schemas, company_schemas

from .models import Company, Storage
# , Supplier, Supply, Product
from .permissions import IsCompanyOwner, IsCompanyStaff
from .serializers import (
    CompanySerializer,
    StorageSerializer
    # SupplierSerializer,
    # SupplySerializer,
    # ProductSerializer
)


class CompanyView(ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()

    def get_queryset(self):
        return Company.objects.filter(owner=self.request.user)

    def get_object(self):
        return Company.objects.filter(owner=self.request.user).first()

    def get_permissions(self):

        if self.action == 'retrieve' or self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsCompanyOwner, IsAuthenticated]
        return [permission() for permission in permission_classes]

    # @extend_schema(
    #     responses=company_schemas.create_put_responses,
    #     request=company_schemas.create_put_request,
    #     description='Создание компании доступно только авторизованным пользователям.'
    # )
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('У Вас уже есть компания.')

        company = serializer.save()

        user = self.request.user
        user.is_company_owner = True
        user.company = company
        user.save(update_fields=['is_company_owner', 'company'])

    # @extend_schema(
    #     responses=company_schemas.delete_response,
    #     description='Удалить компанию может только владелец..'
    # )
    def perform_destroy(self, instance):
        user = self.request.user
        user.is_company_owner = False
        user.company = None

        instance.delete()

    # @extend_schema(
    #     responses=company_schemas.create_put_responses,
    #     request=company_schemas.create_put_request,
    #     description='Изменение данных компании доступно только владельцу.'
    # )


class StorageView(ModelViewSet):
    serializer_class = StorageSerializer
    permission_classes = [IsAuthenticated]
    queryset = Storage.objects.all()

    def get_queryset(self):
        return Storage.objects.filter(company=self.request.user.company)

    def get_permissions(self):

        if self.action == 'retrieve':
            permission_classes = [IsCompanyStaff]
        else:
            permission_classes = [IsCompanyOwner]
        return [permission() for permission in permission_classes]

    # @extend_schema(
    #     responses=storage_schemas.create_put_responses,
    #     request=storage_schemas.create_put_request,
    #     description='Создание склада доступно только владельцу компании.'
    # )
    def perform_create(self, serializer):
        # это необязательное условие, но пока оставлю
        if self.get_queryset().exists():
            raise ValidationError('У Вашей компании уже есть склад.')

        serializer.save(company=self.request.user.company)

# class SupplierViewSet(ModelViewSet):
#     serializer_class = SupplierSerializer
#     permission_classes = [IsAuthenticated, IsCompanyStaff]
#     queryset = Supplier.objects.all()
#
#     def get_queryset(self):
#         return Supplier.objects.filter(company=self.request.user.company).all()
#
#     def perform_create(self, serializer):
#         serializer.save(company=self.request.user.company)
#
#
# class ProductViewSet(ModelViewSet):
#     serializer_class = ProductSerializer
#     permission_classes = [IsCompanyStaff]
#     queryset = Product.objects.all()
#
#     def get_queryset(self):
#         return Product.objects.filter(storage=self.request.user.company.storage).all()
