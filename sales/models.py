from django.db import models
from base.models import Restaurant

# Create your models here.


class Sale(models.Model):
  restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
  income = models.DecimalField(max_digits=8, decimal_places=2)
  sale_datetime = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return str(self.restaurant) if self.restaurant else "No Restaurant"
  