from django.db import models
from django.conf import settings

# Create your models here.
class FileMeta(models.Model):
  file = models.FileField(upload_to='../media/',default='')