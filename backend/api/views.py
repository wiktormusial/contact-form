from rest_framework.views import APIView
from rest_framework.response import Response


class SendMailView(APIView):
    """
    Send an email using mailgun to client email address
    """

    def get(self, request, format=None):
        return Response('Ok')

    def post(self, request, format=None):
        return Response('Ok')
