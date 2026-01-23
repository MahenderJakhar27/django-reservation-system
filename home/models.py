from django.db import models

# Create your models here.
class SampleModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

class Reservation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    guest_count = models.IntegerField()
    reservation_date = models.DateTimeField()
    comments = models.CharField(max_length=200)
    PaymentStatusCode =(
        (0,'Unpaid Bill'),
        (1,'Bill Paid ')
    )
    payment_status=models.IntegerField(choices=PaymentStatusCode, default=0)
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
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.reservation.payment_status = 1
        self.reservation.save()

    def __str__(self):
        return f"Payment for {self.reservation.booking_number}"

     