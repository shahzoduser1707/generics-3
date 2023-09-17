from django.shortcuts import render
from rest_framework.response import Response
from .models import LaptopModel
from .serializers import LaptopSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class GetLaptop(generics.ListAPIView):
    queryset = LaptopModel.objects.all()
    serializer_class = LaptopSerializer
    permission_classes = (IsAuthenticated,)

class CreateLaptop(generics.CreateAPIView):
    queryset = LaptopModel.objects.all()
    serializer_class = LaptopSerializer
    
class GetCreateLaptop(generics.ListCreateAPIView):
    queryset = LaptopModel.objects.all()
    serializer_class = LaptopSerializer

class DetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = LaptopModel.objects.all()
    serializer_class = LaptopSerializer
