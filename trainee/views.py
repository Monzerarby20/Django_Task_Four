from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from .forms import TraineeForm
from course.models import Course  

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/list.html', {'trainees': trainees})

def add_trainee(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST, request.FILES)  # ✅ Add request.FILES
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            course = form.cleaned_data['course']
            image = form.cleaned_data.get('image')  # ✅ Get image from form
            Trainee.objects.create(name=name, email=email, course=course, image=image)  # ✅ Save image
            return redirect('trainee_list')
    else:
        form = TraineeForm()
    return render(request, 'trainee/add.html', {'form': form})

def update_trainee(request, trainee_id):
    trainee = get_object_or_404(Trainee, id=trainee_id)
    if request.method == 'POST':
        form = TraineeForm(request.POST, request.FILES, instance=trainee)  
        if form.is_valid():
            form.save()  
            return redirect('trainee_list')
    else:
        form = TraineeForm(instance=trainee)
    return render(request, 'trainee/update.html', {'form': form})


def delete_trainee(request, trainee_id):
    trainee = get_object_or_404(Trainee, id=trainee_id)
    if request.method == 'POST':
        trainee.delete()
        return redirect('trainee_list')
    return render(request, 'trainee/delete.html', {'trainee': trainee})
