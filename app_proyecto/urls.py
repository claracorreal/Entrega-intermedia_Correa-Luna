from django.urls import path
from app_proyecto.views import index

urlpatterns = [
    path('home/', index),
]