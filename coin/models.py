from django.db import models


class Coin(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    active = models.BooleanField(default=True)
    market_cap = models.FloatField()
    volume = models.FloatField()
    profile = models.ImageField(upload_to='profile_coins/', null=True)

    def __str__(self):
        return f'{self.name} {self.price}'
