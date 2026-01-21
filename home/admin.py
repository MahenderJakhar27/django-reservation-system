from django.contrib import admin
from .models import SampleModel, Reservation, Payment


@admin.register(SampleModel)
class SampleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'guest_count',
        'reservation_date',
        'booking_number',
    )
    search_fields = ('first_name', 'last_name', 'booking_number')
    list_filter = ('reservation_date',)
    inlines = [PaymentInline]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'reservation',
        'amount',
        'payment_date',
    )
