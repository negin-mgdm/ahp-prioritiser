from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Tasks

# Create your views here.


def index(request):
    tasks = Tasks.objects.all()
    return render(request, 'proplanner/index.html', {'tasks': tasks})


def detail(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    return render(request, 'proplanner/detail.html', {'task': task})
