from django import forms
from .models import Trainee
from course.models import Course  

class TraineeForm(forms.ModelForm):  
    class Meta:
        model = Trainee
        fields = ['name', 'email', 'course', 'image']  
