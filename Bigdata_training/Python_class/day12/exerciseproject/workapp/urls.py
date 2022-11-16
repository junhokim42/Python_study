from django.urls import path
from . import views

urlpatterns = [
    path('exercise1/', views.exercise1),
    path('exercise2/', views.exercise2),
    path('exercise3/', views.exercise3),
    path('product1/', views.product1),
    path('basket1/', views.basket1, name = 'basket1'),
]