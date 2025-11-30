
from django.urls import path
from . import views


urlpatterns = [
    path('users/register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.CustomTokenRefreshView.as_view(), name='token_refresh')
    # path('attach-user-to-company/')
]