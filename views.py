from django.shortcuts import render

# Create your views here.
from .models import Prices
from django.http import JsonResponse


def priceslist(request):
	MAX_OBJECTS = 20
	prices = Prices.objects.all()[:20]

	
	data = {"results": list(prices.values())}

	return JsonResponse(data)
    


