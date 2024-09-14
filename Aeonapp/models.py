from django.db import models
class WorkshopDetail(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=800)
    is_active=models.BooleanField(default=True)
# Create your models here.
