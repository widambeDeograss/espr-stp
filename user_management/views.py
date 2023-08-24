from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, ChangePasswordSerializer
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .token import get_user_token
from .models import User
from rest_framework.generics import UpdateAPIView


class RegisterUser(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        data = request.data
        print(request.data)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            username = data['username']
            user = User.objects.filter(username=username)
            if user:
                message = {'status': False, 'message': 'Username already exists'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()

            message = {'save': True}
            return Response(message)

        message = {'save': False, 'errors': serializer.errors}
        return Response(message)


class LoginView(APIView):

    @staticmethod
    def post(request):
        email = request.data.get('email')
        password = request.data.get('password')
        print('Data: ', email, password)
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            user_id = User.objects.get(email=email)
            user_info = UserSerializer(instance=user_id, many=False).data
            response = {
                'token': get_user_token(user_id),
                'user': user_info
            }

            return Response(response)
        else:
            response = {
                'msg': 'Invalid username or password',
            }

            return Response(response)


class UserInformation(APIView):

    @staticmethod
    def get(request, query_type):
        if query_type == 'single':
            try:
                user_id = request.GET.get('user_id')
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({'message': 'User Does Not Exist'})
            return Response(UserSerializer(instance=user, many=False).data)

        elif query_type == 'all':
            queryset = User.objects.all()
            return Response(UserSerializer(instance=queryset, many=True).data)

        else:
            return Response({'message': 'Wrong Request!'})


def statusName(name):
    if name == 0:
        return 'User deleted'
    elif name == 1:
        return 'User disabled'
    elif name == 2:
        return 'User inactive'
    elif name == 3:
        return 'Default status'
    elif name == 4:
        return 'User Active'
    else:
        return 'Invalid Status'


class ChangeStatus(APIView):

    @staticmethod
    def get(request, user_id, status_to):
        try:
            status_name = statusName(status_to)
            if status_name == 'Invalid Status':
                return Response({'message': status_name})

            user = User.objects.get(id=user_id)
            user.status = status_to
            user.save()
            return Response({'message': 'Status changed to ' + status_name})

        except User.DoesNotExist:
            return Response({'message': 'User Does Not Exist'})


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        username = request.data['username']
        email = request.data['email']
        full_name = request.data['full_name']
        phone_number = request.data['phone_number']
        if request.user.username == username:
            try:
                query = User.objects.get(email=email)
                query.email = email,
                query.username = username
                query.full_name = full_name
                query.phone_number = phone_number
                query.save()
                return Response({'message': 'success'})
            except User.DoesNotExist:
                return Response({'message': 'You can not change the email'})

        else:

            return Response({'message': 'Not Authorized to Update This User'})












# import asyncio
# from django.shortcuts import render
# from .serializers import *
# from .models import *
# from rest_framework.views import *
# from  rest_framework.response import *
# from rest_framework.permissions import *
# from rest_framework import *
# from django.contrib.auth import *
# # Create your views here.


# class RegisterUser(APIView):
#     @staticmethod
#     def post(request):
#         data= request.data
#         serializer = UserSerializer(data=data)
        
#         if serializer.is_valid():
#             username = data['username']
#             user = User.objects.filter(username=username) #since username will be the email so no need to check the email
#             if user :
#                 message = {'status': False, 'message': "username alread existed"}
#                 return Response(message, status= status.HTTP_400_BAD_REQUEST)
#             user = serializer.save()
            
#             message = {'save': True}
            
#             return Response (message)
        
#         message = {'save': False, 'errors':serializer.errors}
#         return Response(message)
    
    
    
# class LoginView(APIView):
#     @staticmethod
#     def post(request):
#         username =  request.data.get('username')
#         password =request.data.get('password')
        
#         user = authenticate(username = username , password = password )
#         if user is not None:
#             login(request,user)
#             user_id =User.objects.get(username=username)
#             user_info = UserSerializer(instance=user_id, many=False).data
#             response={
#                 'user':user_info
#             }
            
#             return Response(response)
#         else:
#             response={
#                 'msg':'invalid/wrong username or password'
#             }
#             return Response(response)