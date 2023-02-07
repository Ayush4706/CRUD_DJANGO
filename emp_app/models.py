from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=50,null=False)
    location=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=50,null=False)

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    first_name=models.CharField(max_length=50,null=False)
    last_name=models.CharField(max_length=50)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE,db_constraint=False)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role, on_delete=models.CASCADE,db_constraint=False)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()

    def __str__(self) -> str:
        return self.first_name
