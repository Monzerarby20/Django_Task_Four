from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255, default="Unnamed Course")
    description = models.TextField()
    
    def __str__(self):
        return self.name