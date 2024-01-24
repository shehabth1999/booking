from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from ..models import Trip
from .serializers import TripSerializer
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 30
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'results': data
        })


class TripView(viewsets.ModelViewSet):
    queryset = Trip.get_all()
    serializer_class = TripSerializer
    pagination_class =  CustomPagination
    
  

