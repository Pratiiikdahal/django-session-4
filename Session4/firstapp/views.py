from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Employee
from firstapp.forms import EmployeeForm
from . import forms
from django.http import HttpResponse

# Create your views here.
def index(request):
    context=Employee.objects.all()
    emp_list={'emp_list':context}
    return render(request,'firstapp/index.html',context=emp_list)

def formsIndex(request):
    context={'forms':EmployeeForm}
    if request.method=='POST':
        form=forms.EmployeeForm(request.POST)
        if form.is_valid():
            # Employee.objects.create(ename=form.cleaned_data['EmployeeName'],
            #                         esal=form.cleaned_data['EmployeeSalary'],
            #                         edept=form.cleaned_data['EmployeeDept'],
            #                         eid=form.cleaned_data['EmployeeId'],
            #                         enationality=form.cleaned_data['EmployeeNationality'])
            form.save(commit=True)
            print('done')
            return HttpResponse('Data Saved SuccessFully !!!')
        else:
            print(form.errors)
    return render(request,"firstapp/forms.html",context=context)

