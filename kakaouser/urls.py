from django.urls import path
from .views import *

urlpatterns = [
    path('kakao/login/', kakao_login, name='kakao_login'),
    path('kakao/callback/', kakao_callback, name='kakao_callback'),
    path('kakao/login/finish/', KakaoLogin.as_view(),
         name='kakao_login_todjango'),
]
