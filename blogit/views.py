from rest_framework.response import Response
from rest_framework.views import APIView


class RootRoute(APIView):
    """Root API endpoint that returns a welcome message."""

    def get(self, request):
        return Response({'message': 'Welcome to Blogit API!'})
