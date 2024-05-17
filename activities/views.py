from django.shortcuts import render
from django.http import HttpResponse
from .models import DailyActivity
from rest_framework import viewsets
from .serializers import DailyActivitySerializers
from rest_framework import permissions


class DailyActivityModelViewSet(viewsets.ModelViewSet):
    queryset = DailyActivity.objects.all()
    serializer_class = DailyActivitySerializers

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
