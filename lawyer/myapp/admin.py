from django.contrib import admin
from .models import Lawyer,City,State, Notary
# Register your models here.

admin.site.register(Lawyer)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Notary)