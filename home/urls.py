from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    # pages
    path('reservation/', views.home, name='create_reservation'),
    path('payment/create/', views.create_payment, name='create_payment'),
    path('show-reservations/', views.show_reservations, name='show_reservations'),
    path('payment/show/', views.show_payments, name='show_payments'),

    # APIs
    path('api/login/', views.login_api),
    path('api/reservations/list/', views.reservation_list_api),
    path('api/reservations/create/', views.create_reservation_api),
    path('api/reservations/delete/<int:reservation_id>/', views.delete_reservation),
    path('api/payments/create/', views.create_payment_api),
]
