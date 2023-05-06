from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('work-main/<str:pk>/', views.work_main, name='work-main'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
