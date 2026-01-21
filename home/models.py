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
    booking_number = models.CharField(max_length=100, unique=True, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.booking_number:
            import uuid
            self.booking_number = str(uuid.uuid4())[:8]   # small unique code
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.booking_number})"

class Payment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    print("hi")

     