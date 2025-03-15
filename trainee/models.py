from django.db import models
from course.models import Course
class Trainee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name
