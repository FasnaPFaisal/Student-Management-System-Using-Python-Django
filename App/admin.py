from django.contrib import admin
from .models import AddEmployee, StudentDetails, ContactDetails, Registration

# Register your models here.
admin.site.register(StudentDetails)
admin.site.register(ContactDetails)
admin.site.register(AddEmployee)
admin.site.register(Registration)
