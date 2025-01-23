from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    """Root API endpoint that returns a welcome message."""
    return Response({'message': 'Welcome to Blogit API!'})
