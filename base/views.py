from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant, Rating, Sale
from .serializers import RestaurantSerializer, SaleSerializer, RatingSerializer


# Create your views here.


class RestaurantList(APIView):
    def get(self, request):
        ratings = Restaurant.objects.all()
        serializer = RestaurantSerializer(ratings, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Restaurant registered successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetail(APIView):
    def get(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message" : "Restaurant updated successfully", 
                "data" : serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        restaurant.delete()
        return Response({
            "message" : "Deleted Successfully"
        },status=status.HTTP_204_NO_CONTENT)


class SaleList(APIView):
    def get(self, request):
        restaurant_id = request.query_params.get('restaurant', None)
        if restaurant_id:
            sales = Sale.objects.filter(restaurant__id = restaurant_id)
        else :
            sales = Sale.objects.all()
            
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Sale Record Created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SaleDetail(APIView):
    def get(self, request, pk):
        try:
            sale = Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SaleSerializer(sale)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            sale = Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SaleSerializer(sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message" : "Sale updated successfully", 
                "data" : serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            sale = Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        sale.delete()
        return Response({
            "message" : "Deleted Successfully"
        },status=status.HTTP_204_NO_CONTENT)



class RatingList(APIView):
    def get(self, request):
        user_id = request.query_params.get('user', None)
        restaurant_id = request.query_params.get('restaurant', None)
        
        ratings = Rating.objects.all()
        if user_id:
            ratings = ratings.filter(user__id = user_id)
        if restaurant_id:
            ratings = ratings.filter(restaurant__id = restaurant_id)
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Rating Submitted successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingDetail(APIView):
    def get(self, request, pk):
        try:
            rating = Rating.objects.get(pk=pk)
        except Rating.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            sale = Rating.objects.get(pk=pk)
        except Rating.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RatingSerializer(sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message" : "Rating updated successfully", 
                "data" : serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            rating = Rating.objects.get(pk=pk)
        except Rating.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rating.delete()
        return Response({
            "message" : "Deleted Successfully"
        },status=status.HTTP_204_NO_CONTENT)
