from django.shortcuts import render
from django.http import HttpResponse
from .models import Trainer
from rest_framework import viewsets
from .serializers import TrainerSerializers


class TrainerModelViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializers

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)