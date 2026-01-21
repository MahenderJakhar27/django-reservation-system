from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('function', views.hello_world),
    path('class',views.HelloWorldView.as_view()),
    path('reservation', views.home, name='create_reservation'),    
    path('api/reservations/', views.create_reservation),
    path('api/login/', views.login_api),
    path('api/reservations/get/', views.get_reservations),
    path('api/reservations/delete/<int:reservation_id>/', views.delete_reservation),
    path('show-reservations', views.show_reservations, name='show_reservations'),
    path('payment/create/', views.create_payment, name='create_payment'),
    path('payment/show/', views.show_payments, name='show_payments'),
] 