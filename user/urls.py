from django.urls import path, include
from .views import EmailCheckView

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/checkemail/', EmailCheckView.as_view())
]
