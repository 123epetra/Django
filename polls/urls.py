from django.urls import path

from . import views

urlpatterns = [
    path("index", views.world, name="index"),
    path('register', views.register, name='register'),
]

