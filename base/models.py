from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

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




class Rating(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  rating = models.PositiveSmallIntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
  
  def __str__(self):
    return f"{self.user.username} rated {self.restaurant.name}: {self.rating}"



class Sale(models.Model):
  restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
  income = models.DecimalField(max_digits=8, decimal_places=2)
  sale_datetime = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return str(self.restaurant) if self.restaurant else "No Restaurant"
  