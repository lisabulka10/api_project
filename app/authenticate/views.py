from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserSerializer

from drf_spectacular.utils import (
    extend_schema,
    OpenApiRequest,
    extend_schema_view
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


@extend_schema(
    tags=['register'],
    request=OpenApiRequest(
        request={
            'type': 'object',
            'properties': {
                'username': {
                    'type': 'string',
                    'example': 'user1'
                },
                'email': {
                    'type': 'string',
                    'example': 'example@example.com'
                },
                'password': {
                    'type': 'string',
                    'example': 'password'
                }
            }
        }
    )
)
class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema_view(
    post=extend_schema(
        summary="Получение JWT токенов",
        description="Аутентификация по email и паролю. Возвращает access и refresh токены.",
        tags=["authenticate"]
    )
)
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema_view(
    post=extend_schema(
        summary="Обновление access токена",
        description="Обновление access токена по refresh токену.",
        tags=["authenticate"]
    )
)
class CustomTokenRefreshView(TokenRefreshView):
    pass
