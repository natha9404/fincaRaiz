from django.db import models

# Create your models here.
class Categories (models.Model):
    slug = models.CharField(verbose_name="Slug", max_length=500 )