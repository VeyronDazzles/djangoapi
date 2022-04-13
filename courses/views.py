# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from .models import course
from .serializers import courseSerializer

class courseView(viewsets.ModelViewSet):
    queryset = course.objects.all()
    serializer_class = courseSerializer
