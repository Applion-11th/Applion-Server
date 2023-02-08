import email
from rest_framework.viewsets import ModelViewSet
from .serializers import ApplicationSerializer
from .models import Application

class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    # lookup_field = email