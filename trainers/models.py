from django.db import models

# Create your models here.
class Trainer(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True) 
    profile_picture = models.ImageField(upload_to='trainers/profile_pictures/', blank=True)
    certification = models.CharField(max_length=50, blank=True) 
    specialization = models.CharField(max_length=50, blank=True) 
    experience = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username