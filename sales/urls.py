from django.urls import path
from .views import SaleDetail, SaleList

urlpatterns = [
    path('sales/', SaleList.as_view(), name='sale-list'),
    path('sales/<int:pk>/', SaleDetail.as_view(), name='sale-detail')
]
