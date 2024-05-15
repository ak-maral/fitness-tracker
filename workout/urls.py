from rest_framework import routers
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
# router.register('workout', views.WorkoutViewSet, basename='Workout')

urlpatterns = [
    # path("workout/", WorkoutModelViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'}), name="workout"),
    path('workout/', views.WorkoutListViewSet.as_view()),
    path('workout/', views.WorkoutCreateViewSet.as_view()),
    path('workout/<int:pk>/', views.WorkoutDetailViewSet.as_view()),
    # path('workout/', views.WorkoutViewSet.as_view()),
    # path('', include(router.urls)),
    # path('workout/', views.WorkoutViewSet.as_view()),
    # path('workout/', views.WorkoutViewSet.as_view()),
    # path('workout/<int:pk>/', views.WorkoutViewSet.as_view(),),
    # path("workout/<int:pk>/", WorkoutListViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="workout")
]

urlpatterns += router.urls