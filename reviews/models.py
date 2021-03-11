from django.db import models

# Create your models here.
class Reviews (models.Model):
    feedback = models.TextField(verbose_name="Feedback")
    rating = models.IntegerField()
    avatar = models.URLField(verbose_name="Avatar")