from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserSerializer

from drf_spectacular.utils import (
    extend_schema,
    OpenApiRequest,
)


@extend_schema(
    tags=['Users'],
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
                    'example': 'example@examle.com'
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
