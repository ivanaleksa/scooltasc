from django.urls import path
from . import views

app_name = 'schedule'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:schedule_id>/', views.DetailSchedule, name='DetailSchedule'),
]