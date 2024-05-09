from rest_framework import routers
from django.urls import path
from .views import TrainerModelViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path("user/", TrainerModelViewSet.as_view({'get': 'list', 'post': 'create'}), name="user"),
    path("user/<int:pk>/", UserModelViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="user")
]

urlpatterns += router.urls