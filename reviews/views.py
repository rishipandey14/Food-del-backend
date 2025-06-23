from rest_framework.views import APIView
from .models import Rating
from .serializers import RatingSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

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
    
    def patch(self, request, pk):
        try:
            sale = Rating.objects.get(pk=pk)
        except Rating.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RatingSerializer(sale, data=request.data, partial=True)
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
