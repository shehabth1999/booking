from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripView

router = DefaultRouter()
router.register('', TripView, basename='trip')


urlpatterns = [
    path('',include(router.urls))
]
