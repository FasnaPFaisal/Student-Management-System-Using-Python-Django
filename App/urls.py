
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="home"),   
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('register/',views.register,name="register"), 
    path('addemp/',views.addemp,name="addemp"),
    path('delete/<id>',views.delete, name="delete"),
    path('update/<id>',views.update, name="update")
]


