from django.shortcuts import render,redirect
from .models import ContactDetails, StudentDetails,Registration,AddEmployee
from .forms import RegistrationForm

# Create your views here.
def index(request):     
    registrations = Registration.objects.all() 
    return render(request,"index.html",{'registrations' : registrations})

def about(request):
    student_details = StudentDetails.objects.all()
    return render(request,"about.html",{'student': student_details})

def contact(request):
    contact_details = ContactDetails.objects.all()
    return render(request,"contact.html",{'contact': contact_details})


def addemp(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        name = request.POST.get('name')        
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')
        date_of_joining = request.POST.get('date_of_joining')
        role = request.POST.get('role')
        AddEmployee.objects.create(employee_id = employee_id,name = name,address = address,email = email,
                                   contact_number = contact_number,date_of_joining = date_of_joining,role = role)
        return redirect("home")
    return render(request,"addemp.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {'form': form})

def update(request,id):
    registrations = Registration.objects.get(id = id)
    if request.method == 'POST':
        registrations.register_no = request.POST.get('register_no')
        registrations.name = request.POST.get('name')
        registrations.age = request.POST.get('age')
        registrations.email = request.POST.get('email')
        registrations.phone_number = request.POST.get('phone_number')
        registrations.save()        
        return redirect("home")
    return render(request, "update.html", {'registrations': registrations})

def delete(request,id):
    registrations = Registration.objects.get(id = id)
    registrations.delete()
    return redirect("home")
