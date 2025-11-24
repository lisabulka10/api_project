from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.exceptions import ValidationError, NotFound
from django.shortcuts import render
from .models import Company, Storage
from .permissions import IsCompanyOwner
from .serializers import CompanySerializer, StorageSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


class CompanyView(RetrieveModelMixin,
                  GenericViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Company.objects.filter(owner=self.request.user)

    @action(methods=['post'], detail=False, url_path='create')
    def create_company(self, request, *args, ** kwargs):
        if self.get_queryset().exists():
            raise ValidationError('У Вас уже есть компания.')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['delete'], detail=False, permission_classes=[IsCompanyOwner], url_path='delete')
    def delete_company(self, request):
        instance = self.get_object()
        if not instance:
            raise NotFound('Компания не найдена')
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['put'], detail=False, permission_classes=[IsCompanyOwner], url_path='update')
    def update_company(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)



# class CompanyRetrieveView(RetrieveModelMixin,
#                           GenericAPIView):
#     serializer_class = CompanySerializer
#
#     def get_queryset(self):
#         return Company.objects.filter(owner=self.request.user)
#
#
# class CompanyCreateView(CreateModelMixin,
#                         GenericViewSet):
#     serializer_class = CompanySerializer
#
#     def get_queryset(self):
#         return Company.objects.filter(owner=self.request.user)
#
#     def perform_create(self, serializer):
#         if self.get_queryset().exists():
#             raise ValidationError('У Вас уже есть компания.')
#         serializer.save(owner=self.request.user)
#
#
# class CompanyDeleteView(DestroyModelMixin,
#                         GenericViewSet):
#     serializer_class = CompanySerializer
#
#     def get_queryset(self):
#         return Company.objects.filter(owner=self.request.user)
#
#     def perform_delete(self, serializer):
#         if self.get_queryset().exists():
#             raise ValidationError('У Вас уже есть компания.')
#         serializer.save(owner=self.request.user)
#
#
# class CompanyView(CreateModelMixin,
#                   RetrieveModelMixin,
#                   DestroyModelMixin,
#                   UpdateModelMixin,
#                   GenericViewSet):
#     serializer_class = CompanySerializer
#     lookup_field = 'pk'
#
#     def get_queryset(self):
#         return Company.objects.filter(owner=self.request.user)
#
#     def perform_create(self, serializer):
#         if self.get_queryset().exists():
#             raise ValidationError('У Вас уже есть компания.')
#         serializer.save(owner=self.request.user)
