from django.db import models
from moviepy.editor import VideoFileClip

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

    def save(self, *args, **kwargs):
        if self.video_file:
            # Open the video file and get its duration
            try:
                clip = VideoFileClip(self.video_file.path)
                self.duration = clip.duration
            except Exception as e:
                # Handle any exceptions that may occur during duration extraction
                # You might want to log the error or take other appropriate actions
                pass

        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
