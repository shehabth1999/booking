from django.contrib import admin
from trip.models import Trip as model, Area as model2

@admin.register(model)
class ModelAdmin(admin.ModelAdmin):
    search_fields   = model.search_fields
    list_filter     = model.list_filter
    list_display    = model.list_display 

@admin.register(model2)
class ModelAdmin(admin.ModelAdmin):
    search_fields   = model2.search_fields

