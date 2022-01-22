from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SendMailSerializer


class SendMailView(APIView):
    """
    Send an email using mailgun to client email address
    """

    def get(self, request, format=None):
        return Response('Ok')

    def post(self, request, format=None):
        serializer = SendMailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
