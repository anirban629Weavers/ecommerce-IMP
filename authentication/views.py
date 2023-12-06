from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .serializers import RegistrationSerializer
from rest_framework.throttling import ScopedRateThrottle

class RegisterAPI(generics.CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class=RegistrationSerializer
    
class LoginAPI(TokenObtainPairView):
    throttle_classes=[ScopedRateThrottle]
    permission_classes=[AllowAny]
    throttle_scope = 'cust'