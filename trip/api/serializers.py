from rest_framework import serializers
from ..models import Trip, Area, Language_Trip
from authentication.models import User

class LanguageTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language_Trip
        fields = ('name', 'description')

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'name', 'description']

class TripSerializer(serializers.ModelSerializer):
    from_area = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    to_area = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    status = serializers.CharField(source='get_status_display', read_only=True)
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False)

    class Meta:
        model = Trip
        fields = '__all__'

    def validate_users(self, value):
        trip_instance = self.instance

        if trip_instance and hasattr(trip_instance, 'seat'):
            max_users = trip_instance.seat

            if len(value) > max_users:
                raise serializers.ValidationError(f'This Trip Has Reached Maximum Number of Seats')
        return value