from rest_framework import serializers
from .models import Workout


class WorkoutCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('name','type', 'descriprion', 'videl_file', 'image', 'duration','user')

