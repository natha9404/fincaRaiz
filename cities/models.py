from django.db import models

from states.models import States
# Create your models here.
class Cities (models.Model):
    slug = models.CharField(verbose_name="Slug", max_length=500 )
    code_zip = models.TextField(verbose_name="Zip")
    state = models.ForeignKey(States, on_delete=models.CASCADE)