from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def root_route(_):
    return Response(
        {
            'message': 'Welcome to the Blogit API.',
            'version': '1.0.0',
            'status': 'OK',
        },
        status=status.HTTP_200_OK,
    )
