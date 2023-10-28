from django.contrib import admin
from .models import Lawyer,City,State, Notary
from . import models
# Register your models here.

@admin.register(models.Lawyer)

class LawyerAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'case_type'

    ]

@admin.register(models.City)

class CityAdmin(admin.ModelAdmin):
    list_display = [
        'city_name',
        'city_no'

    ]

@admin.register(models.State)

class StateAdmin(admin.ModelAdmin):
    list_display = [
        'state_name',
        'state_no',
    ]
@admin.register(models.Notary)

class NotaryAdmin(admin.ModelAdmin):
    list_display = [
        'Name',
        'reg_no',
        'address',
    ]