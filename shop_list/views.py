from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import django_filters
from rest_framework import viewsets, filters
from .models import Shoptext
from .serializer import ShoptextSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ShoptextViewSet(viewsets.ModelViewSet):
    queryset=Shoptext.objects.all()
    serializer_class=ShoptextSerializer

