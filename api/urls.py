# api/urls.py
from django.urls import path
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ListReceivedData.as_view()),
    path('<int:pk>/', views.DetailReceivedData.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]