from django.urls import path
from .views import *

urlpatterns = [
    path('', Appview, name='Appview'),
    path('back/', Backview, name='Backview'),
    path('front/', Frontview, name='Frontview'),
    path('make-csv/', make_csv, name='make_csv'),
]
