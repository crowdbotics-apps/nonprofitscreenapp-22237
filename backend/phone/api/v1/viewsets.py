from rest_framework import authentication
from phone.models import Call
from .serializers import CallSerializer
from rest_framework import viewsets


class CallViewSet(viewsets.ModelViewSet):
    serializer_class = CallSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Call.objects.all()
