from django.urls import path
from .views import CreateCategoryView, GetCategoryByIdView, CreatePostView, GetCategoryListView, GetPostByIdView, GetPostListView


urlpatterns = [
    path('create-category/', CreateCategoryView.as_view(), name='create-category'),
    path('category/<int:c_id>/', GetCategoryByIdView.as_view(), name='category'),
    path('categories/', GetCategoryListView.as_view(), name='category-list'),
    path('create/', CreatePostView.as_view(), name='create-post'),
    path('<int:post_id>/', GetPostByIdView.as_view(), name='post-by-id'),
    path('list/', GetPostListView.as_view(), name='post-list'),
    
]