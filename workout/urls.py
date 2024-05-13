from rest_framework import routers
from django.urls import path
from .views import WorkoutModelViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path("workout/", WorkoutModelViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'}), name="user"),
    path("workout/<int:pk>/", WorkoutModelViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="user")
]

urlpatterns += router.urls