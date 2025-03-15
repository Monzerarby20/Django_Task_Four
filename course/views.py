from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Course

class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'course/list.html'
    context_object_name = 'courses'

class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'course/add.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('course_list')

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    template_name = 'course/update.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('course_list')

class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'course/delete.html'
    success_url = reverse_lazy('course_list')
