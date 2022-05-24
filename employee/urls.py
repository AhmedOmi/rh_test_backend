from django.views.generic import TemplateView
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.list, name='list_employees'),
    path('success',TemplateView.as_view(template_name='success.html')),
    path('add/', views.CreateEmployee, name='create_employee'),
    path('employees/', views.EmployeesList.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
