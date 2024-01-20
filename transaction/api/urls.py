from django.urls import path, include
from .views import TransactionView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TransactionView, basename='transactions')

urlpatterns = [
    path('',include(router.urls))
]
