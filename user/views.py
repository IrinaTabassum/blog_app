from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from .models import User

# Create your views here.
class RegisterView(APIView):
    def post(self, request, format=None):
        print("post")
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(username=serializer.validated_data['username'], email=serializer.validated_data['email'], password=request.data.get('password'))
            # serializer.validated_data['password'] = make_password(request.data.get('password'))
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserListView(APIView):
    def get(self, request, format=None):
        users = User.objects.all() 
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetUserByIdView(APIView):
    def get(self, request, user_id, format=None):
        print(user_id)
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"massage":"user not found"}, status=status.HTTP_404_NOT_FOUND)
        

class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)
    
    
    def patch(self, request, format=None):
        try:
            user = request.user
            IsPasswordMatch = check_password(request.data.get('old_password'), user.password)
            if(IsPasswordMatch):
                if request.data.get('new_password') == request.data.get('confirm_password'):
                    user.set_password(request.data.get('new_password'))
                    user.save()
                else :
                    return Response({"massage":"Confirm password is not mach"}, status=status.HTTP_409_CONFLICT)
            else:
                return Response({"massage":"Password is not currect"}, status=status.HTTP_409_CONFLICT)
            
            return Response({"massage":"Password is update"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"massage":"user not found"}, status=status.HTTP_404_NOT_FOUND)
        

class LogOutView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        try:
            # print(request.user.refresh_token)
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            print(token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
class UserUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def patch(self, request):
        try:
            user = request.user
            print(request.user.id)
            user.first_name = request.data.get('first_name')
            user.last_name = request.data.get('last_name')
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)     