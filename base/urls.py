from django.urls import path
from .views import RestaurantList, RestaurantDetail


urlpatterns = [
  path('restaurants/', RestaurantList.as_view()),
  path('restaurants/<int:pk>/', RestaurantDetail.as_view()),
]
