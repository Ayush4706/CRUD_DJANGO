from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
import emp_app

from emp_app.models import Employee,Department,Role

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emp=Employee.objects.all()
    context={
        'emps':emp,
    }
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=int(request.POST['role'])
        dept=int(request.POST['dept'])
        phone=int(request.POST['phone'])
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,role_id=role,dept_id=dept,phone=phone,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('<h3>Employee Added successfully</h3>') 
    else:
        return render(request,'add_emp.html')

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_removed=Employee.objects.get(id=emp_id)
            emp_removed.delete()
            return HttpResponse('<h3>Employee has been deleted')
        except:
            return HttpResponse("Select a valid employee id")
    emp=Employee.objects.all()
    context={
        'emps':emp
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name=dept)
        if role:
            emps=emps.filter(role__name=role)

        context={
            'emps':emps
        }
        return render(request,'all_emp.html',context)
    elif request.method=='GET':
        return render(request,'filter.html')
    else:
        return HttpResponse('<h1>NOT Found</h1>')
