from django.contrib import admin
from .models import Appointment,Contact

admin.site.register(Contact)  
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=('name','email','date','time','status')  

# Register your models here.
