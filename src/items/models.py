from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()

    class Meta:
        db_table = "item"
