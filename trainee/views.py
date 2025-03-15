from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Trainee
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin




class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'trainee/register.html'
    success_url = reverse_lazy('login')  


class UserLoginView(LoginView):
    template_name = 'trainee/login.html'


class UserLogoutView(LogoutView):
    next_page = 'login'  


class TraineeListView(LoginRequiredMixin, ListView):
    model = Trainee
    template_name = 'trainee/list.html'
    context_object_name = 'trainees'

class TraineeListView(LoginRequiredMixin, ListView):
    model = Trainee
    template_name = 'trainee/list.html'
    context_object_name = 'trainees'


class TraineeCreateView(LoginRequiredMixin, CreateView):
    model = Trainee
    template_name = 'trainee/add.html'
    fields = ['name', 'email', 'phone', 'course']
    success_url = reverse_lazy('trainee_list')


class TraineeUpdateView(LoginRequiredMixin, UpdateView):
    model = Trainee
    template_name = 'trainee/edit.html'
    fields = ['name', 'email', 'phone', 'course']
    success_url = reverse_lazy('trainee_list')


class TraineeDeleteView(LoginRequiredMixin, DeleteView):
    model = Trainee
    template_name = 'trainee/delete.html'
    success_url = reverse_lazy('trainee_list')
