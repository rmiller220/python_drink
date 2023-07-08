from django.http import JsonResponse
# from django.shortcuts import render
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
    drinks = Drink.objects.all()   #get all drinks from db
    serialized_drinks = DrinkSerializer(drinks, many=True)   #serialize the drinks
    return JsonResponse({'drinks': serialized_drinks.data}) #return a json response with serialized drinks #safe=False is required for objects that are not dictionaries
