from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
        
    def create(self, validated_data):
        # Don't include 'update_at' when creating a new post
        validated_data.pop('update_at', None)
        return super().create(validated_data)

