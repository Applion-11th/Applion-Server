from .models import User
from rest_framework import serializers
from application.models import Application
from dj_rest_auth.registration.serializers import RegisterSerializer


class SignupSerializer(RegisterSerializer):
    #회원가입 하면 자동으로 지원서 모델 생성
    def custom_signup(self, request, user):
        Application(user=user).save()
        return super().custom_signup(request, user)
 

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'student_num', 'semester', 'major', 'phone_num', 'position')

class IDCheckSerializer(serializers.Serializer):
    is_unique = serializers.BooleanField()