from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        default="https://example.com/placeholder.png",
    )

    def __str__(self):
        return f"{self.name} - {self.price} {self.image}"
