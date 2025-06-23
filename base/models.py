from django.db import models

# Create your models here.

class Restaurant(models.Model):
  
  class TypeChoices(models.TextChoices):
    INDIAN = 'IN', 'Indian'
    CHINESE = 'CH', 'Chinese'
    THAI = 'TH', 'Thai'
    OTHER = 'OT', 'Other'
  
  
  name = models.CharField(max_length=200)
  website = models.URLField(blank=True, null=True)
  date_opened = models.DateField()
  latitude = models.FloatField()
  longitude = models.FloatField()
  restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)
  
  def __str__(self):
    return self.name
  
  class Meta:
    constraints = [
      models.UniqueConstraint(fields=['name', 'longitude', 'latitude'], name='unique_named_location')
    ]


class Staff(models.Model):
  name = models.CharField(max_length=200)
  restaurants = models.ManyToManyField(Restaurant)

