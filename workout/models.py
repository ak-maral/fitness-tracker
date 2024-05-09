from django.db import models
from trainers.models import Trainer

class Workout(models.Model):
    BEGINNER = 'beginner'
    INTERMEDIATE = 'intermediate'

    WORKOUT_TYPE_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=WORKOUT_TYPE_CHOICES, default='beginner')
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    duration = models.FloatField(default=0)  # Duration of the video in seconds
    trainer = models.ForeignKey(to = Trainer, on_delete=models.SET_NULL, null=True, related_name="trainer")

    def __str__(self):
        return self.name