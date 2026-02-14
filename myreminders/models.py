from django.db import models
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date=models.DateField()
    time=models.TimeField()
    phone=models.CharField(max_length=20)
    status=models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name