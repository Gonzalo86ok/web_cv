from django.db import models

# Create your models here.

class CV(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    mail = models.EmailField()
    adress = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    professional_experience = models.TextField()
    skill = models.CharField(max_length=200)

    def __str__(self):
        return self.name