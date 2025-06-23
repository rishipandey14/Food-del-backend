from django.urls import path
from .views import RatingDetail, RatingList

urlpatterns = [
    path('ratings/', RatingList.as_view(), name='rating-list'),
    path('ratings/<int:pk>/', RatingDetail.as_view(), name='rating-detail'),
]
