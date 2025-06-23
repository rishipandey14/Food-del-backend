from django.urls import path
from .views import RestaurantList, RestaurantDetail, SaleList, SaleDetail, RatingList, RatingDetail


urlpatterns = [
  path('restaurants/', RestaurantList.as_view(), name='restaurant-list'),
  path('restaurants/<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail'),
  
  path('sales/', SaleList.as_view(), name='sale-list'),
  path('sales/<int:pk>', SaleDetail.as_view(), name='sale-detail'),
  
  path('ratings/', RatingList.as_view(), name='rating-list'),
  path('ratings/<int:pk>', RatingDetail.as_view(), name='rating-detail'),
  
]
