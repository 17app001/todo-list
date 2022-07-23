from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('view/<int:id>', views.view, name='view'),
    path('create/', views.create, name='create'),
    path('completed/', views.completed, name='completed')
]
