from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
  
urlpatterns = [
    path('employees/', views.EmployeesList.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetails.as_view()),
]
  
urlpatterns = format_suffix_patterns(urlpatterns)