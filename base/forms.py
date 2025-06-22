from django import forms
from base.models import Rating

class RatingForm(forms.ModelForm):
  class Meta:
    model = Rating
    fields = ('restaurant', 'user', 'rating')