from django.db import models


# Create your models here.

class Destination:
    id: int
    name: str
    desc: str
    img_name: str
    price: int
    offer: bool


class Destinations(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=200)
    desc = models.TextField()
    img_name = models.ImageField(upload_to="pics")
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
