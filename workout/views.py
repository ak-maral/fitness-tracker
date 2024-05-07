from django.shortcuts import render, get_object_or_404, redirect
from .models import Workout
from .forms import CreateWorkoutForm

def home(request):
    return render(request, 'workout/home.html')

def workouts(request):
    workouts = Workout.objects.all()
    return render(request, 'workout/workouts.html', {'workouts': workouts})

def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    return render(request, 'workout/workout_detail.html', {'workout': workout})

def create_workout(request):
    if request.method == 'POST':
        form = CreateWorkoutForm(request.POST, request.FILES)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.video_file = request.FILES['video']  # Associate the uploaded video file with the Workout instance
            workout.save()
            return redirect('workouts')
    else:
        form = CreateWorkoutForm()
    return render(request, 'workout/create_workout.html', {'form': form})

def edit_workout(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    if request.method == 'POST':
        form = CreateWorkoutForm(request.POST, request.FILES, instance=workout)
        if form.is_valid():
            # Associate the uploaded video file with the Workout instance
            workout.video_file = request.FILES.get('video_file')
            form.save()
            # Recalculate and update duration if needed
            if 'video_file' in form.changed_data:
                try:
                    clip = VideoFileClip(workout.video_file.path)
                    workout.duration = clip.duration
                except Exception as e:
                    # Handle any exceptions that may occur during duration extraction
                    pass
            workout.save()
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = CreateWorkoutForm(instance=workout)
    
    return render(request, 'workout/edit_workout.html', {'form': form})

def delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    if request.method == 'POST':
        workout.delete()
        return redirect('workouts')
    return render(request, 'workout/delete_workout.html', {'workout': workout})

