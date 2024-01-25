from django.db import models
from django.shortcuts import get_object_or_404
from authentication.models import User
from datetime import timedelta
from .controller.create import Malti_Create_ALl_DBs

class Area(models.Model):
    id =                models.AutoField(primary_key=True)
    name =              models.CharField(max_length=30, unique=True)
    description =       models.CharField(max_length=1000, null = True)
    created_at =        models.DateTimeField(auto_now_add=True)
    objects =           Malti_Create_ALl_DBs()
    search_fields = [
       'name',
    ]
    def __str__(self) :
        return self.name


class Trip(models.Model):
    STATUS_CHOICES = (
        (1, "Planned"),
        (2, "In Progress"),
        (3, "Completed"),
        (4, "Cancelled"),
        (5, "Delayed"),
        (6, "On Hold"),
        (7, "Expired"),
    )

    id =            models.AutoField(primary_key=True)
    users =         models.ManyToManyField(User)
    seat =          models.IntegerField(default=20)
    name =          models.CharField(max_length=30)
    description =   models.CharField(max_length=1000, null=True, blank=True)
    from_area =     models.ForeignKey(Area, on_delete=models.CASCADE, related_name='trips_from')
    to_area =       models.ForeignKey(Area, on_delete=models.CASCADE, related_name='trips_to')
    start_time =    models.DateTimeField()
    end_time =      models.DateTimeField()
    bus_number =    models.CharField(max_length=30)
    status =        models.IntegerField(choices=STATUS_CHOICES, default = 1)
    price =         models.IntegerField(null=True, blank=True)
    created_time =  models.DateTimeField(auto_now_add=True)
    updated_time =  models.DateTimeField(auto_now=True)
    objects =       Malti_Create_ALl_DBs()


    search_fields = [
       'name',
    ]

    list_filter = [
        'users',
    ]

    list_display = [
        'name',
        'from_area',
        'to_area',
    ]

    def __str__(self):
        return self.name
    
    @classmethod
    def get_element_by_id(cls, pk):
        return get_object_or_404(cls, pk=pk)
    
    @classmethod
    def get_all(cls):
        return cls.objects.all().order_by('id')
    
    @classmethod
    def get_all_second_db(cls):
        return cls.objects.using('second').all().order_by('id')
    
    @classmethod
    def filter_by_from_area(cls,from_area):
        return cls.objects.filter(from_area=from_area).order_by('id')
    
    @classmethod
    def filter_by_to_area(cls,to_area):
        return cls.objects.filter(to_area=to_area).order_by('id')
    
    @classmethod
    def filter_by_status(cls,status):
        return cls.objects.filter(status=status).order_by('id')
    
    @classmethod
    def filter_by_price_min_max(cls,min_price, max_price):
        return cls.objects.filter(price__gte=min_price, price__lte=max_price).order_by('price')
    

    @classmethod
    def filter_by_start_date(cls, date):
        return cls.objects.filter(start_time__date=date).order_by('start_time')

    @classmethod
    def filter_by_end_date(cls, date):
        return cls.objects.filter(end_time__date=date).order_by('end_time')

    @classmethod
    def filter_by_start_to_end(cls, start_date, end_date):
        date_range = (start_date, end_date + timedelta(days=1))
        return cls.objects.filter(start_time__range=date_range, end_time__range=date_range).order_by('start_time')
    
    