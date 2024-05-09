from django.shortcuts import render
from .models import Workout
from .serializers import WorkoutSerializers
from rest_framework import viewsets

# Create your views here.
class WorkoutModelViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializers

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)