from django.shortcuts import render, redirect
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/list.html', {'courses': courses})

def add_course(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        start_date = request.POST['start_date']
        Course.objects.create(title=title, description=description, start_date=start_date)
        return redirect('course_list')
    return render(request, 'course/add.html')
