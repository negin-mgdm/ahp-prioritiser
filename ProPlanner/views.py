import random
from django.http import JsonResponse
from django.shortcuts import render
from .models import Item


def index(request):
    return render(request, 'index.html')


def get_items(request):
    categories = Item.objects.values_list('category', flat=True).distinct()

    if categories:
        selected_category = random.choice(categories)

        items_in_category = Item.objects.filter(category=selected_category)

        if items_in_category:
            selected_items = random.sample(
                list(items_in_category), min(len(items_in_category), 5))

            items_data = [{'id': item.id, 'title': item.title, 'score': item.score,
                           'category': item.category} for item in selected_items]

            return JsonResponse(items_data, safe=False)

    return JsonResponse([], safe=False)
