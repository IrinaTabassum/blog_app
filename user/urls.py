from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView, 
)
from .views import RegisterView, UserListView, GetUserByIdView, ChangePasswordView, LogOutView, UserUpdateView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('register/', RegisterView.as_view(), name='user-register'),
    path('list/', UserListView.as_view(), name='user-list'),
    path('<int:user_id>/', GetUserByIdView.as_view(), name='get-user-by-id'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('logout/', LogOutView.as_view(), name='auth_logout'),
    path('update/', UserUpdateView.as_view(), name='user-update'),

]