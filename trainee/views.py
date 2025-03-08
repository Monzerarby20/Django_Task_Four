from django.shortcuts import render, redirect
from .models import Trainee

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/list.html', {'trainees': trainees})

def add_trainee(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        Trainee.objects.create(name=name, email=email, age=age)
        return redirect('trainee_list')
    return render(request, 'trainee/add.html')
