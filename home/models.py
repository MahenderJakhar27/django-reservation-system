from django.db import models

# Create your models here.
class SampleModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

class Reservation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    guest_count = models.IntegerField()
    reservation_date = models.DateTimeField(auto_now=True)
    commants = models.CharField(max_length=200)

     