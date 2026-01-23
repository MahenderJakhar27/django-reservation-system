from rest_framework import serializers
from .models import Reservation

class ReservationListSerializer(serializers.ModelSerializer):
    payment_status_label = serializers.CharField(
        source='get_payment_status_display',
        read_only=True
    )

    class Meta:
        model = Reservation
        fields = [
            'id',
            'first_name',
            'last_name',
            'guest_count',
            'reservation_date',
            'comments',
            'booking_number',
            'payment_status',
            'payment_status_label',
        ]

class ReservationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'first_name',
            'last_name',
            'guest_count',
            'reservation_date',
            'comments',
        ]
