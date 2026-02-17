from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date=models.DateField()
    time=models.TimeField()
    phone=models.CharField(max_length=20)

    SERVICE_CHOICES=[('Doctor','Doctor'),
                     ('Office Interview','Office Interview'),
                     ('Business Meeting','Business Meeting'),
                    ('Beauty Parlour','Beauty Parlour'),
                    ]
    service=models.CharField(max_length=50,choices=SERVICE_CHOICES)
    
    STATUS_CHOICES=[('Pending','Pending'),
                    ('Approved','Approved'),
                    ('Rejected','Rejected'),
                    ('Completed','Completed'),]
    status=models.CharField(max_length=20,choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
