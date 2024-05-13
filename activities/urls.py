from rest_framework import routers
from django.urls import path
from .views import DailyActivityModelViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path("activity/", DailyActivityModelViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'}), name="user"),
    path("activity/<int:pk>/", DailyActivityModelViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="user")
]

urlpatterns += router.urls