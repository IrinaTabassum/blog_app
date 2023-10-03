from django.urls import path
from .views import CreateCategoryView, GetCategoryByIdView, CreatePostView


urlpatterns = [
    path('create-category/', CreateCategoryView.as_view(), name='create-category'),
    path('category/<int:c_id>/', GetCategoryByIdView.as_view(), name='category'),
    path('create/', CreatePostView.as_view(), name='create'),

]