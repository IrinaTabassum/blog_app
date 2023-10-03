from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CategorySerializer, PostSerializer
from .models import Category, Post

# Create your views here.

class CreateCategoryView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetCategoryByIdView(APIView):
     def get(self, c_id):
        try:
            category = Category.objects.get(id=c_id)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"massage":"Category not found"}, status=status.HTTP_404_NOT_FOUND)


class CreatePostView(APIView):
    
    def post(self, request):
        try:
            category = Category.objects.get(id=request.data.get("category_id"))
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, category=category)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:  
            print(e)  
            
