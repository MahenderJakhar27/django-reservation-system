from rest_framework import serializers
from .models import Reservation, Payment

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

class PaymentCreateSerializer(serializers.ModelSerializer):
    reservation_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Payment
        fields = ['reservation_id', 'amount']

    def validate_reservation_id(self, value):
        try:
            reservation = Reservation.objects.get(id=value)
        except Reservation.DoesNotExist:
            raise serializers.ValidationError("Reservation not found")

        if reservation.payment_status == 1:
            raise serializers.ValidationError("Reservation is already paid")

        # store for reuse
        self.reservation = reservation
        return value

    def create(self, validated_data):
        payment = Payment.objects.create(
            reservation=self.reservation,
            amount=validated_data['amount']
        )
        return payment
