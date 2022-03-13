from django.contrib import admin
from .models import *


class ClientList(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'DOB', 'gender', 'zip', 'phone')
    list_filter = ('fname', 'lname', 'phone')
    search_fields = ('fname', 'lname', 'phone')
    ordering = ('fname', 'lname', 'phone')


class VolunteerList(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'phone')
    list_filter = ('fname', 'lname', 'phone')
    search_fields = ('fname', 'lname', 'phone')
    ordering = ('fname', 'lname', 'phone')
# We might want to add in days the volunteers are normally available


class VisitList(admin.ModelAdmin):
    list_display = ('visit_note', 'date', 'client', 'volunteer', 'employee')
    list_filter = ('date', 'client')
    search_fields = ('date', 'client')
    ordering = ('date', 'client')


class InventoryList(admin.ModelAdmin):
    list_display = ('UPScode', 'item_description')
    list_filter = ('UPScode', 'item_description')
    search_fields = ('UPScode', 'item_description')
    ordering = ('UPScode', 'item_description')


class OrdersList(admin.ModelAdmin):
    list_display = ('client', 'UPScode', 'item_description', 'request_quantity', 'delivered_quantity', 'date')
    list_filter = ('client', 'UPScode', 'item_description', 'request_quantity', 'delivered_quantity', 'date')
    search_fields = ('client', 'UPScode', 'item_description', 'request_quantity', 'delivered_quantity', 'date')
    ordering = ('client', 'UPScode', 'item_description', 'request_quantity', 'delivered_quantity', 'date')


admin.site.register(Client)
admin.site.register(Volunteer)
admin.site.register(Visit)
admin.site.register(Inventory)
admin.site.register(Order)

