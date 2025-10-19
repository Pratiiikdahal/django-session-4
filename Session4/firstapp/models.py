from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=100)
    edept=models.CharField(max_length=100)
    esal=models.FloatField()
    eid=models.IntegerField()
    enationality=models.CharField(max_length=100)
    
    def __str__(self):
        return self.ename