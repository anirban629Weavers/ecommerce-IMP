from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,mixins,serializers
from .serializers import OrderSerializer
from core.models import Order
from rest_framework_simplejwt.authentication import JWTAuthentication 

class OrderView(mixins.CreateModelMixin,GenericViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    
        