from django.http import HttpResponse
from django.shortcuts import render
from .models import Tasks

# Create your views here.


def index(request):
    tasks = Tasks.objects.all()
    return render(request, 'proplanner/index.html', {'tasks': tasks})
