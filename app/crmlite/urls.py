from rest_framework.routers import SimpleRouter
from django.urls import path, include
from . import views


COMPANIES_PREFIX = 'companies'
STORAGES_PREFIX = 'storages'
SUPPLIER_PREFIX = 'suppliers'
PRODUCT_PREFIX = 'products'

# product_detail_view = views.ProductViewSet.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})

urlpatterns = [
    path(f'{COMPANIES_PREFIX}/<int:pk>/', views.CompanyView.as_view({'get': 'retrieve'}), name='companies-details'),
    path(f'{COMPANIES_PREFIX}/create/', views.CompanyView.as_view({'post': 'create'}), name='companies-create'),
    path(f'{COMPANIES_PREFIX}/delete/', views.CompanyView.as_view({'delete': 'destroy'}), name='companies-delete'),
    path(f'{COMPANIES_PREFIX}/update/', views.CompanyView.as_view({'put': 'update'}), name='companies-update'),

    path(f'{STORAGES_PREFIX}/<int:pk>/', views.StorageView.as_view({'get': 'retrieve'}), name='storage-details'),
    path(f'{STORAGES_PREFIX}/<int:pk>/delete', views.StorageView.as_view({'delete': 'destroy'}), name='storage-delete'),
    path(f'{STORAGES_PREFIX}/<int:pk>/update', views.StorageView.as_view({'put': 'update'}), name='storage-update'),
    path(f'{STORAGES_PREFIX}/create/', views.StorageView.as_view({'post': 'create'}), name='storage-create'),

    # path(f'{SUPPLIER_PREFIX}/list/', views.SupplierViewSet.as_view({'get': 'list'}), name='supplier-list'),
    # path(f'{SUPPLIER_PREFIX}/create/', views.SupplierViewSet.as_view({'post': 'create'}), name='supplier-create'),
    # path(f'{SUPPLIER_PREFIX}/<int:pk>/update/', views.SupplierViewSet.as_view({'put': 'update'}),
    #      name='supplier-detail'),
    # path(f'{SUPPLIER_PREFIX}/<int:pk>/delete/', views.SupplierViewSet.as_view({'delete': 'destroy'}),
    #      name='supplier-destroy'),
    #
    # path(f'{PRODUCT_PREFIX}/<int:pk>/', product_detail_view, name='product-detail'),
    # path(f'{PRODUCT_PREFIX}/add/', views.ProductViewSet.as_view({'post': 'create'}), name='product-create'),
    # path(f'{PRODUCT_PREFIX}/list/', views.ProductViewSet.as_view({'get': 'list'}), name='product-list'),
]
#urlpatterns += router.urls

