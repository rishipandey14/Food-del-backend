from django.db import models
from django.contrib.auth.models import User
from base.models import Restaurant
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Rating(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  rating = models.PositiveSmallIntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
  
  def __str__(self):
    return f"{self.user.username} rated {self.restaurant.name}: {self.rating}"

