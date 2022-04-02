from django.contrib import admin

# Register your models here.
from demo_tu.models import Car, CarAdmin

admin.site.register(Car, CarAdmin)