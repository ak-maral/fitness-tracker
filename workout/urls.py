from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('workouts/', views.workouts, name='workouts'),
    path('workout/<int:workout_id>/', views.workout_detail, name='workout_detail'),
    path('new/', views.create_workout, name='create_workout'),
    path('<int:workout_id>/edit/', views.edit_workout, name='edit_workout'),
    path('<int:workout_id>/delete/', views.delete_workout, name='delete_workout'),
    # Add more paths for your views as needed
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
