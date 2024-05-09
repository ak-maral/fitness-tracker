from django.db import models
from workout.models import Workout

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    age = models.IntegerField(null=True, blank=True)  
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    workout = models.ForeignKey(to = Workout, on_delete=models.SET_NULL, null=True, related_name="workout")

    def __str__(self):
        return self.username
