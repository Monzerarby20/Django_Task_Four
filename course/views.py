from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm
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

def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')  
    else:
        form = CourseForm(instance=course)  
    
    return render(request, 'course/update.html', {'form': form})

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        course.delete()
        return redirect('course_list')
    return render(request, 'course/delete.html', {'course': course})
