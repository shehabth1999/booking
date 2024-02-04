from django.contrib import admin
from trip.models import Trip as model, Area as model2, Language_Trip, Language_Area

@admin.register(model)
class ModelAdmin(admin.ModelAdmin):
    search_fields   = model.search_fields
    list_display    = model.list_display 

@admin.register(model2)
class ModelAdmin(admin.ModelAdmin):
    search_fields   = model2.search_fields
admin.site.register(Language_Trip)
admin.site.register(Language_Area)
