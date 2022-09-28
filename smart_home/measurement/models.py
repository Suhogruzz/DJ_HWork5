from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)


class Measurements(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(blank=True)