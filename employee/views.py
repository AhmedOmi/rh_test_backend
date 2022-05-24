from django.shortcuts import render, redirect
from django.http import Http404
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
import employee
from employee.forms import EmployeeForm
from .models import Employee
from .serializers import EmployeeSerializer
from django.template import loader


def list(request):
    list_employees = Employee.objects.all()
    template = loader.get_template('list.html')
    context = {
        'list_employees': list_employees,
    }
    return HttpResponse(template.render(context, request))


def CreateEmployee(request):
    if request.method == "GET":
        form = EmployeeForm
        context = {
            'form': form,
        }
        return render(request, "add.html", context)
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_employees')

def show(request,id):
    context ={}
    context["data"] = Employee.objects.get(id=id)
    return render(request, "details.html", context)

class EmployeesList(APIView):
    """
    List all Employees, or create a new Employes
    """

    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetails(APIView):
    """
    Retrieve, update or delete an Employee instance
    """

    def get_object(self, pk):
        # Returns an object instance that should
        # be used for detail views.
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee,
                                        data=request.data,
                                        partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
