from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from django.contrib import messages


# Create your views here.
from employee.models import Employee


def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass

    else:
        form = EmployeeForm()
        return render(request, 'index.html', {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, 'show.html', {"employees": employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid:
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {employee: employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            return redirect('/show')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')
