from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from drf_spectacular.utils import extend_schema

from .models import Company, Storage
from .permissions import IsCompanyOwner
from .serializers import CompanySerializer, StorageSerializer
from .schemas import storage_schemas, company_schemas


class CompanyView(RetrieveModelMixin,
                  GenericViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()

    def get_queryset(self):
        return Company.objects.filter(owner=self.request.user)

    @extend_schema(
        responses=company_schemas.create_put_responses,
        request=company_schemas.create_put_request,
        description='Создание компании доступно только авторизованным пользователям.'
    )
    @action(methods=['post'], detail=False, url_path='create')
    def create_company(self, request, *args, ** kwargs):
        if self.get_queryset().exists():
            raise ValidationError('У Вас уже есть компания.')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        company = serializer.save()

        user = request.user
        user.is_company_owner = True
        user.company = company
        user.save(update_fields=['is_company_owner', 'company'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        responses=company_schemas.delete_response,
        description='Удалить компанию может только владелец..'
    )
    @action(methods=['delete'], detail=False, permission_classes=[IsCompanyOwner], url_path='delete')
    def delete_company(self, request):
        instance = self.get_queryset().first()
        if not instance:
            raise NotFound('Компания не найдена')
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        responses=company_schemas.create_put_responses,
        request=company_schemas.create_put_request,
        description='Изменение данных компании доступно только владельцу.'
    )
    @action(methods=['put'], detail=False, permission_classes=[IsCompanyOwner], url_path='update')
    def update_company(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_queryset().first()
        if not instance:
            raise NotFound('Компания не найдена.')
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class StorageView(RetrieveModelMixin,
                  GenericViewSet):
    serializer_class = StorageSerializer
    permission_classes = [IsAuthenticated]
    queryset = Storage.objects.all()

    def get_queryset(self):
        return Storage.objects.filter(company=self.request.user.company)

    @extend_schema(
        responses=storage_schemas.create_put_responses,
        request=storage_schemas.create_put_request,
        description='Создание склада доступно только владельцу компании.'
    )
    @action(methods=['post'], detail=False, url_path='create', permission_classes=[IsCompanyOwner])
    def create_storage(self, request):
        if self.get_queryset().exists():
            raise ValidationError('У Вашей компании уже есть склад.')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(company=request.user.company)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        responses=storage_schemas.create_put_responses,
        request=storage_schemas.create_put_request,
        description='Изменение данных склада доступно только владельцу компании.'
    )
    @action(methods=['put'], detail=True, permission_classes=[IsCompanyOwner], url_path='update')
    def update_storage(self, request, pk, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_queryset().filter(id=pk).first()
        if not instance:
            raise NotFound('Склад не найден.')
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @extend_schema(
        responses=storage_schemas.delete_response,
        description='Удаление склада доступно только владельцу компании.'
    )
    @action(methods=['delete'], detail=True, permission_classes=[IsCompanyOwner], url_path='delete')
    def delete_storage(self, request, pk):
        instance = self.get_queryset().filter(id=pk).first()
        if not instance:
            raise NotFound('Склад не найден')
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
