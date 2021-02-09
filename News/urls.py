from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.NewView.as_view()),
    path('<int:pk>/', views.NewDetail.as_view(), name='detail'),
]