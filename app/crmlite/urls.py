from rest_framework.routers import SimpleRouter
from django.urls import path, include
from . import views

router = SimpleRouter()
router.register(r'companies', views.CompanyView, basename='company')

urlpatterns = router.urls
# from django.urls import path
# from .views import CompanyView
#
# company_view = CompanyView.as_view()
#
# urlpatterns = [
#     path('companies/', company_view, name='company-create'),          # POST
#     path('companies/<int:pk>/', company_view, name='company-detail'), # GET, PUT, PATCH, DELETE
# ]
