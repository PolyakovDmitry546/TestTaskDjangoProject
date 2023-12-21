from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()

    class Meta:
        db_table = "item"

    def __str__(self) -> str:
        return f"{self.name}: {self.price}"
