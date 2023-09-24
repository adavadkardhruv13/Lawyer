from django.db import models

# Create your models here.
class State(models.Model):
    state_no = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=200)


    def __str__(self):
        return self.state_name

class City(models.Model):
    state = models.ManyToManyField(State)
    city_no = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=200)


    def __str__(self):
        return self.city_name

class Lawyer(models.Model):
    city = models.ManyToManyField(City)
    state = models.ManyToManyField(State)
    name = models.CharField(max_length=200)
    case_type = models.CharField(max_length=200)
    phone_no = models.IntegerField(max_length=10)


    def __str__(self):
        return self.name
