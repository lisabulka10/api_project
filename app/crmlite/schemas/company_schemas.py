from drf_spectacular.utils import (
    extend_schema,
    OpenApiRequest,
    OpenApiResponse
)

create_put_request = OpenApiRequest(
    request={
        'type': 'object',
        'properties': {
            'INN': {
                'type': 'string',
                'example': '157987032237'
            },
            'title': {
                'type': 'string',
                'example': 'ОАО Компания'
            }
        },
    }
)

create_put_responses = {
    201: OpenApiResponse(
        response={
            'type': 'object',
            'properties': {
                'id': {'type': 'integer', 'example': 1},
                'title': {'type': 'string', 'example': 'ОАО Компания'},
                'INN': {'type': 'string', 'example': '157987032237'}
            }
        },
        description='Компания успешно создана'
    ),
    400: OpenApiResponse(
        response={
            'type': 'object',
            'properties': {
                'detail': {'type': 'string', 'example': 'У вас уже есть компания'},
            }
        },
        description='Ошибка при создании компании.'
    )
}

delete_response = {
    204: OpenApiResponse(
        response={
            'type': 'object',
            'properties': {
                'id': {'type': 'integer', 'example': 1},
                'title': {'type': 'string', 'example': 'ОАО Компания'},
                'INN': {'type': 'string', 'example': '157987032237'}
            }
        },
        description='Компания успешно удалена.'
    ),
    404: OpenApiResponse(
        response={
            'type': 'object',
            'properties': {
                'detail': {'type': 'string', 'example': 'Компания не найдена'},
            }
        },
        description='Ошибка при удалении компании.'
    )
}




