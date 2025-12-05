from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Reservation
from .serializers import ReservationSerializer
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, World!")

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("this is mahender jakhar")
    
def home(request):
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Reservation created successfully!") 
    return render(request, 'create_reservation.html', {'form': form})

@api_view([ 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_reservation(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Reservation created successfully","data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view([ 'GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_reservations(request):
    reservations = Reservation.objects.all().values()
    return JsonResponse(list(reservations), safe=False)
    
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_reservation(request, reservation_id):
    try:
        reservation = Reservation.objects.get(id=reservation_id)
        reservation.delete()
        return JsonResponse(
            {"message": "Reservation deleted successfully"},
            status=status.HTTP_200_OK
        )
    except Reservation.DoesNotExist:
        return JsonResponse(
            {"error": "Reservation not found"},
            status=status.HTTP_404_NOT_FOUND
        )
def index(request):
    return render(request, 'home_page.html')
def show_reservations(request):
    reservations = Reservation.objects.all().order_by('-id')
    return render(request, 'show_reservations.html', {'reservations': reservations})

@api_view(['POST'])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "username": user.username})

    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
