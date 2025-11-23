from django.urls import path
from . import views


urlpatterns = [
    path('function', views.hello_world),
    path('class',views.HelloWorldView.as_view()),
    path('reservation', views.home, ),       
    path('api/reservations/', views.create_reservation),
    path('api/reservations/get/', views.get_reservations),
] 