from django.shortcuts import render
from .models import Student 
def index(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        phoneno=request.POST['phoneno']
        date=request.POST['date']
        student=Student(name=name,names=password,namess=phoneno,namesss=date)
        student.save()
    return render(request,('index.html'))
