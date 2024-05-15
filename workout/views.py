# from django.shortcuts import render
# from .models import Workout
# from .serializers import WorkoutSerializers, WorkoutCreateSerializers
# from rest_framework import viewsets
# from rest_framework import permissions

# # class WorkoutListViewSet(viewsets.ModelViewSet):
# #     queryset = Workout.objects.all()
# #     serializer_class = WorkoutSerializers

# #     def get_permissions(self):
# #         return permissions.AllowAny()
    
# class WorkoutViewSet(viewsets.ModelViewSet):
#     queryset = Workout.objects.all()
#     serializer_class = WorkoutSerializers

#     def get_serializer_class(self):
#         if self.action == ('retrieve',):
#             return WorkoutSerializers
#         elif self.action == ('create','update', 'partial_update','delete'):
#             return WorkoutCreateSerializers

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
