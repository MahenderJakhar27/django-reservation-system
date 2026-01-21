from django import forms
from .models import Reservation,Payment

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['reservation','amount']