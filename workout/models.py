from django.db import models

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

    def __str__(self):
        return self.name
