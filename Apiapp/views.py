from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Data
from Api.serializers import DataSerealizer
from rest_framework import generics
# Create your views here.

class Dataview(generics.ListCreateAPIView):

	queryset = Data.objects.all()
	serializer_class = DataSerealizer

class Datadetailview(generics.RetrieveUpdateDestroyAPIView):
	queryset = Data.objects.all()
	serializer_class = DataSerealizer