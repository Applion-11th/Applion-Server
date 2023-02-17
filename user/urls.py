from django.urls import path, include
from .views import IDCheckView

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/checkid/', IDCheckView.as_view())
]
