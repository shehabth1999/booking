from django.contrib import admin
from book.models import Transaction as model

@admin.register(model)
class ModelAdmin(admin.ModelAdmin):
    search_fields   = model.search_fields
    list_filter     = model.list_filter
    list_display    = model.list_display