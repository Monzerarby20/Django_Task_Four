from django.db import models

class Trainee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    image = models.ImageField(upload_to='trainee_images/', blank=True, null=True)
    def __str__(self):
        return self.name
