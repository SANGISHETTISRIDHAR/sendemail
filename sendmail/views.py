
from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView

from sendemail import settings
from .models import Employee
from sendmail.form import Employeeform
from django.core.mail import send_mail

# Create your views here.
def showindex(request):
    form=Employeeform()
    return render(request,'index.html',{"form":form})
def showindex1(request):
    idno=request.POST.get('idno')
    name=request.POST.get('name')
    email=request.POST.get('email')
    send_mail('registration mail', "Hello Dear "+name+"your email password is changed recently. if you are not changed please change now ", settings.EMAIL_HOST_USER,[email])
    Employee(idno=idno,name=name,email=email).save()
    form =Employeeform()
    return render(request,'index.html',{"form":form})