from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('User/create', views.create_user),
]
