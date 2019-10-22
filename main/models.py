from django.db import models
from django.utils import timezone

# Create your models here.
class Cards(models.Model):
    name = models.CharField(max_length = 200, blank=True, null=True,default='')
    price = models.CharField(max_length = 200, blank=True, null=True,default='')
    rent = models.CharField(max_length = 200, blank=True, null=True,default='')
    number = models.CharField(max_length = 200, blank=True, null=True,default='')
    video_link = models.CharField(max_length = 200, blank=True, null=True,default='')
    description = models.TextField(blank=True,null=True,default='')
    occupied = models.BooleanField(blank=True,null=True,default=False)
    occupier = models.CharField(max_length = 200, blank=True, null=True,default='')

    def publish(self):
        self.time = timezone.now()
        self.save()

    def __str__(self):
        return self.number

class Player(models.Model):
    name = models.CharField(max_length = 200, blank=True, null=True,default='Player1')
    points = models.CharField(max_length = 200, blank=True, null=True,default='')
    wealth = models.CharField(max_length = 200, blank=True, null=True,default='30000')

    def publish(self):
        self.time = timezone.now()
        self.save()

    def __str__(self):
        return self.name
