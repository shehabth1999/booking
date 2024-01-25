from rest_framework import serializers
from ..models import Trip, Area


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'name', 'description']        

class TripSerializer(serializers.ModelSerializer):
    from_area = AreaSerializer()
    to_area = AreaSerializer()
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Trip
        fields = '__all__'

