from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include("user.urls")),
    path('api/user/', include("allauth.urls")),
    path('api/kuser/', include("kakaouser.urls")),
    path('api/application/', include("application.urls")),
]
