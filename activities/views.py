from django.shortcuts import render
from django.http import HttpResponse
from .models import DailyActivity
from rest_framework import viewsets
from .serializers import DailyActivitySerializers


class DailyActivityModelViewSet(viewsets.ModelViewSet):
    queryset = DailyActivity.objects.all()
    serializer_class = DailyActivitySerializers

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)