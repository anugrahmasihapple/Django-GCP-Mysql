from django.db import models

# Create your models here.
class Polls(models.Model):
          name = models.CharField(max_length=30)
          vote = models.BooleanField(default=False)
