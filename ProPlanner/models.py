from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title
