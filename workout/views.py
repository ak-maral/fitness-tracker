from django.shortcuts import render
from .models import Workout
from .serializers import WorkoutSerializers,WorkoutCreateSerializers
from rest_framework import generics
from rest_framework import permissions

class WorkoutListViewSet(generics.ListAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializers

    def get_permissions(self):
        return [permissions.AllowAny()]

class WorkoutCreateViewSet(generics.GenericAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutCreateSerializers

    def get_permissions(self):
        return [permissions.IsAdminUser()]
    
class WorkoutDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializers

    def get_permissions(self):
        return [permissions.IsAdminUser()]
