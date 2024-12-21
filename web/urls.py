# Create web/urls.py and paste the following
from django.urls import path
from . import views


app_name = "web"

urlpatterns = [
      path('', StudentListView.as_view(), name='student_list'),
]
