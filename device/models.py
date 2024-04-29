from django.db import models

# Create your models here.
class Device(models.Model):
    id = models.IntegerField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    index = models.CharField(max_length=12)
    time = models.DateTimeField(auto_now=True)
    image_url = models.CharField(max_length=500)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=12)
    enabled = models.BooleanField(default=True)
    video_url = models.CharField(max_length=500)
    
    class Meta:
        db_table = 'cameras'

class Incident(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=45)
    latitude = models.DecimalField(max_digits=9, decimal_places=1)
    longitude = models.DecimalField(max_digits=9, decimal_places=1)

    class Meta:
        db_table = 'incidents'