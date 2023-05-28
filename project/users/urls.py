from django.urls import path
from .views import *

urlpatterns = [
    path('', RegisterUsers.as_view(), name='register'),
]