from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    pass

class ContactDetails(models.Model):
    pass

class AddEmployee(models.Model):
    employee_id = models.IntegerField() 
    name = models.CharField(max_length=100)    
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_joining = models.DateField()
    role = models.CharField(max_length=50)

class Registration(models.Model):
    register_no = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)