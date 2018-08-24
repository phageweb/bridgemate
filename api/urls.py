# api/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListReceivedData.as_view()),
    path('<int:pk>/', views.ReceivedData.as_view()),
]