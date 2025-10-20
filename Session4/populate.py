from faker import *

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Session4.settings')

import django 
django.setup()

import random

from firstapp.models import *
fake=Faker()


def populate(n):
    
    nationalities = [
    'American', 'German', 'French', 'Japanese', 'Indian', 'Nepali',
    'Chinese', 'Brazilian', 'Canadian', 'Italian', 'Spanish'
    ]
    departments = [
        'HR', 'Finance', 'IT', 'Engineering', 'Marketing', 'Sales',
        'Research', 'Operations', 'Customer Support', 'Legal', 'Administration'
    ]
    for i in range(n):
        fname=fake.name()
        fsal=random.randint(10000,20000000)
        fdept=random.choice(departments)
        fid=random.randint(200,30000)
        fnationality=random.choice(nationalities)
        
        Employee.objects.create(ename=fname,esal=fsal,edept=fdept,eid=fid,enationality=fnationality)
        
populate(100)