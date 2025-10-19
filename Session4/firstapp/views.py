from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Employee
# Create your views here.
def index(request):
    context=Employee.objects.all()
    emp_list={'emp_list':context}
    return render(request,'firstapp/index.html',context=emp_list)