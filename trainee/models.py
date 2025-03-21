from django.db import models
from course.models import Course

class Track(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Trainee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    track = models.ForeignKey(Track, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
