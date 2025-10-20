from django import forms


'''class Employee(models.Model):
    ename=models.CharField(max_length=100)
    edept=models.CharField(max_length=100)
    esal=models.FloatField()
    eid=models.IntegerField()
    enationality=models.CharField(max_length=100)'''
    
    
class EmployeeForm(forms.Form):
    EmployeeName=forms.CharField()
    EmployeeDept=forms.CharField()
    EmployeeSalary=forms.FloatField()
    EmployeeId=forms.IntegerField()
    EmployeeNationality=forms.CharField()
        