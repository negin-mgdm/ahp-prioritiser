from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/items/', views.get_items, name='get_items'),
]
