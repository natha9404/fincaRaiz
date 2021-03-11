from django.db import models

from cities.models import Cities
from categories.models import Categories
# Create your models here.
class Properties (models.Model):
    title = models.CharField(verbose_name="Title", max_length=500)
    image = models.URLField(verbose_name="Image")
    price = models.IntegerField()
    baths = models.IntegerField()
    beds = models.IntegerField()
    sqft = models.IntegerField()
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)