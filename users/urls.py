from rest_framework import routers
from django.urls import path
from .views import UserModelViewSet

router = routers.DefaultRouter()

router.register(
    "users", viewset=UserModelViewSet, basename="users"
)

urlpatterns= [

]

urlpatterns += router.urls