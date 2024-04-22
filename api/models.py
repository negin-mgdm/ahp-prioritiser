from django.db import models
from tastypie.resources import ModelResource
from ProPlanner.models import Tasks


class TaskResource(ModelResource):
    class Meta:
        queryset = Tasks.objects.all()
        resource_name = 'ProPlanner'
