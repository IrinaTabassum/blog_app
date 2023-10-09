from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializer import CategorySerializer, PostSerializer
from .models import Category, Post

# Create your views here.

class CreateCategoryView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetCategoryByIdView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, c_id):
        try:
            category = Category.objects.get(id=c_id)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"massage":"Category not found"}, status=status.HTTP_404_NOT_FOUND)


class GetCategoryListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        try:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"massage":"Somthing is weong"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class CreatePostView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        try:
            category = Category.objects.get(id=request.data.get("category_id"))
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, category=category, update_at="")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:  
            print(e)  
            
class GetPostByIdView(APIView):
    
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"massage":"Post not found"}, status=status.HTTP_404_NOT_FOUND)


class GetPostListView(APIView):
    
    def get(self, request):
        try:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"massage":"Something is wrong"}, status=status.HTTP_404_NOT_FOUND)

  
            
