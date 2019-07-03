from django import forms
from sendmail.models import Employee

class Employeeform(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['idno','name','email']