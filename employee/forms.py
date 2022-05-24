from django.forms import ModelForm, DateInput
from .models import Employee


class DateInput(DateInput):
    input_type = 'date'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {'birthday': DateInput(), 'hired_on': DateInput(),}
