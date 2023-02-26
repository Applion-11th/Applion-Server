from django.urls import path
from .views import Appview

urlpatterns = [
    path('', Appview, name='Appview')
]
