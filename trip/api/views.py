from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from ..models import Trip ,Area ,Language_Trip
from .serializers import TripSerializer, LanguageTripSerializer
from ..controller.pagination import CustomPagination
from rest_framework.decorators import action
from django.utils.translation import activate


class TripView(viewsets.ModelViewSet):
    
    queryset = Trip.get_all()

    serializer_class = TripSerializer
    pagination_class =  CustomPagination
    # @action(detail=False, methods=[''])


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    


    def retrieve(self, request, *args, **kwargs):
        language = kwargs.get('language', 'en')
        activate(language)
        instance = self.get_object()
        language_data = Language_Trip.objects.filter(language = language, trip = instance).first()
        # serializer = self.get_serializer(instance)
        trip_serializer = TripSerializer(instance)
        try:
            language_trip_serializer = LanguageTripSerializer(language_data)
        except Language_Trip.DoesNotExist:
            raise Response({"error": "No data available for this language"},status=404)      
        # response_data = {
        #     'trip': trip_serializer.data,
        #     'language_trip': language_trip_serializer.data if language_data else None,
        # }
        response_data = {
            "trip": {
                "id": trip_serializer.data['id'],
                'name': language_trip_serializer.data['name'],
                "description": language_trip_serializer.data['description'],
                "from_area": trip_serializer.data['from_area'],
                "to_area": trip_serializer.data['to_area'],
                "status": trip_serializer.data['status'],
                "seat": trip_serializer.data['seat'],
                "start_time": trip_serializer.data['start_time'],
                "end_time": trip_serializer.data['end_time'],
                "bus_number": trip_serializer.data['bus_number'],
                "price": trip_serializer.data['price'],
                "created_time": trip_serializer.data['created_time'],
                "updated_time": trip_serializer.data['updated_time'],
                "users": trip_serializer.data['users'],
            }
        }
        return Response(response_data)