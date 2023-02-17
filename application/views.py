import email
from rest_framework.viewsets import ModelViewSet
from .serializers import ApplicationSerializer
from .models import Application
from rest_framework.permissions import IsAuthenticated

class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (IsAuthenticated, )
