# Create web/urls.py and paste the following
from django.urls import path
from . import views


app_name = "web"

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
]