from django.db import models

from propertytypes.models import PropertyTypes

# Create your models here.
class Transactions (models.Model):
    slug = models.CharField(verbose_name="Feedback", max_length=100)
    property_types = models.ManyToManyField(PropertyTypes)