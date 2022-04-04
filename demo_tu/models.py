from django.contrib import admin
from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=200, default=None)
    seats = models.IntegerField(max_length=200, default=None)
    bodyStyle = models.CharField(max_length=200, default=None)
    price = models.FloatField(max_length=200, default=None)
    saleOff = models.FloatField(max_length=200, default=None)
    addedDate = models.DateTimeField()
    note = models.CharField(max_length=200, default=None, blank=True)


class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'seats', 'bodyStyle', 'price']
    search_fields = ['name', 'bodyStyle']
    list_filter = ['bodyStyle', 'addedDate']
    date_hierarchy = 'addedDate'
    actions_on_top = True
    actions_on_bottom = False
