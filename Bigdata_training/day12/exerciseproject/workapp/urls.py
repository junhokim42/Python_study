from django.urls import path
from . import views

urlpatterns = [
    path('exercise1/', views.exercise1),
    path('exercise2/', views.exercise2),
    path('exercise3/', views.exercise3),
]