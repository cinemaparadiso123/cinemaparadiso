from django.shortcuts import render
from rest_framework import generics
from .models import Categories
# Create your views here.
class CategoriesList(generics.ListAPIView):
    queryset = Categories.objects.order_by("created_at").all()