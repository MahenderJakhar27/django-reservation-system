from django import forms
from .models import Reservation,Payment

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'reservation_date': forms.DateInput(attrs={
                'id': 'reservation_date',
                'class': 'form-control',
                'placeholder': 'Select date'
            })
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['reservation','amount']