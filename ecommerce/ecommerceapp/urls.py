from django.contrib import admin
from django.urls import path
from .views import Tamazonview

urlpatterns = [
    path('ecommerce/',Tamazonview.as_view())
]
