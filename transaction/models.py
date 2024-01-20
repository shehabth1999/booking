from django.db import models
from authentication.models import User
from trip.models import Trip
from django.shortcuts import get_object_or_404


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_trnasction')
    amount = models.IntegerField(default=0)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='trip_transction')
    discount = models.FloatField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)

    search_fields  = [ 
    ]

    list_filter = [
        'user',
    ]

    list_display = [
        'user',
        'created_time',
    ]
    def __str__(self):
        return f'{self.user}paid {self.amount} for {self.trip}'

    @classmethod
    def get_element_by_id(cls, transaction_id):
        return get_object_or_404(cls, pk=transaction_id)
    
    @classmethod
    def get_all(cls):
        return cls.objects.all().order_by('id')
    
    @classmethod
    def filter_by_trip(cls,trip_id):
        return cls.objects.filter(trip_id=trip_id).order_by('id')