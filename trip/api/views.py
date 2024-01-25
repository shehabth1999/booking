from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from ..models import Trip ,Area
from .serializers import TripSerializer
from ..controller.pagination import CustomPagination
from rest_framework.decorators import action


class TripView(viewsets.ModelViewSet):
    
    queryset = Trip.get_all()

    serializer_class = TripSerializer
    pagination_class =  CustomPagination
    # @action(detail=False, methods=[''])