from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import EmailCheckSerializer, SignupSerializer


class EmailCheckView(RetrieveAPIView):
    queryset = None
    serializer_class = EmailCheckSerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        email = self.request.data['email']
        try :
            instance = dict()
            SignupSerializer.validate_email(self, email)
            instance['is_unique'] = True
        except Exception as e:
            instance['is_unique'] = False

        serializer = self.get_serializer(instance)
        return Response(serializer.data)