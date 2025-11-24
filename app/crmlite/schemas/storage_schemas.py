from rest_framework import serializers

from ..serializers import StorageSerializer

from drf_spectacular.utils import (
    extend_schema,
    OpenApiRequest,
    OpenApiResponse
)

create_put_request = OpenApiRequest(
    request={
        'type': 'object',
        'properties': {
            'address': {
                'type': 'string',
                'example': 'Санкт-Петербург, Шоссейная д. 7 стр. 4.'
            },
        },
    }
)

create_put_responses = {
    201: OpenApiResponse(response=StorageSerializer, description='Склад успешно зарегистрирован.'),
    400: OpenApiResponse(
        response={
            'type': 'object',
            'properties': {
                'detail': {'type': 'string', 'example': 'У вас уже есть склад.'},
            }
        },
        description='Ошибка при создании склада.'
    )
}

delete_response = {
    204: OpenApiResponse(
        response=StorageSerializer,
        description='Склад успешно удален.'
    ),
    404: OpenApiResponse(
        response={
            'type': 'object',
            'properties': {
                'detail': {'type': 'string', 'example': 'Склад не найден'},
            }
        },
        description='Ошибка при удалении склада.'
    )
}




