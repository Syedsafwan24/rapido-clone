from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(DriverDetails)
admin.site.register(ContactQuery)
admin.site.register(RideRequest)
