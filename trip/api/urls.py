from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripView

router = DefaultRouter()
router.register('', TripView, basename='trip')


urlpatterns = [
    path('',include(router.urls)),
    path('<int:pk>/<str:language>/', TripView.as_view({'get': 'retrieve'}), name='trip-detail'),
    path('<str:language>/', TripView.as_view({'post': 'create', 'get': 'list'}), name='trip-list'),
]
