from django.db import models
from course.models import Course 

class Trainee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='trainee_images/', blank=True, null=True) 

    def __str__(self):
        return self.name
