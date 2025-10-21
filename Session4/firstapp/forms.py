from django import forms
import string 
from firstapp.models import *

# class EmployeeForm(forms.Form):
#     EmployeeName=forms.CharField(label='Employee Name')
#     EmployeeDept=forms.CharField(label='Employee Department')
#     EmployeeSalary=forms.FloatField(label='Employee Salary')
#     EmployeeId=forms.IntegerField(label='Employee ID')
#     EmployeeNationality=forms.CharField(label='Employee Nationality')
#     Password=forms.CharField(widget=forms.PasswordInput , label='Password') 
    
    
#     def clean_EmployeeName(self):
#         emp_name= self.cleaned_data["EmployeeName"]
#         if len(emp_name) < 5:
#             raise forms.ValidationError('The Name that you provided must be greater than 5 words !')
#         return emp_name
    
#     def clean_EmployeeDept(self):
#         emp_dept=self.cleaned_data['EmployeeDept']
#         symbols=string.punctuation
#         symbols=list(symbols)
#         sym_len=len(symbols)
#         emp_dept_list=list(emp_dept)
#         dept_word_count=len(emp_dept_list)
#         for i in range(dept_word_count):
#             print(f"Checking character: {repr(emp_dept_list[i])}")
#             for j in range(sym_len):
#                 if emp_dept_list[i]==symbols[j]:
#                     raise forms.ValidationError('The Department name contains Symbols.Please Enter a valid Name')
#         return emp_dept         
    
    
    
#     def clean_EmployeeNationality(self):
#                 emp_nat=self.cleaned_data['EmployeeNationality']
#                 symbols=string.punctuation
#                 symbols=list(symbols)
#                 sym_len=len(symbols)
                
#                 num=string.digits
#                 num=list(num)
#                 num_len=len(num)
                
#                 emp_nat_list=list(emp_nat)
#                 dept_word_count=len(emp_nat_list)
#                 for i in range(dept_word_count):
#                     for j in range(sym_len):
#                          if emp_nat_list[i]==symbols[j]:
#                             raise forms.ValidationError('The Department name contains Symbols.Please Enter a valid Name')
#                     for k in range(num_len):
#                         if emp_nat_list[i]==num[k]:
#                             raise forms.ValidationError('The Input Contains Numbers. Please enter a valid input')
#                 return emp_nat    

                
            
#creating the model forms here in python

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        # fields include garna tuple ma lekhne 
        # fields exclude garna exclude= vanera list ma lekhne 
        
        