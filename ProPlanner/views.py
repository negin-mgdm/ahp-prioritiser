from django.shortcuts import render
from django.http import JsonResponse
from .models import Item


def index(request):
    return render(request, 'index.html')


def get_items(request):
    items = list(Item.objects.all().values())
    return JsonResponse(items, safe=False)
