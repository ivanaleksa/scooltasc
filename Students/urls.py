from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ListStudent),
    path('<int:id>/', views.DetailStudent, name='studentdetail'),
]