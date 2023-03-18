from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .models import User
from django.contrib.auth import authenticate, login, logout
# authenticate : username과 password를 받는 function, 두 가지 정보가 맞으면 user정보를 return한다.
# login : 로그인 시킬 user와 requst를 보내면 django 브라우저가 필요한 쿠키와 토큰 등 필요한걸 만들어준다.


class Me(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(
            user,
            data = request.data,
            parial = True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class Users(APIView):
    # 유효성 검사는 ModelSerializer가 수행해준다(normal model). 때문에 개발자는 password관리만 해주면된다.
    # 유저가입시 json형태로 일반 모델정보 + pw가 들어올텐데, pw -> hash처리가 되어야 한다.
    def post(self, request):
        password = request.data.get('password')
        if not password:
            raise ParseError
        # 여기까지가 password custom 영역
        serializer = serializers.PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password) # set_password를 통해 raw password를 hash처리한다.
            user.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class LogIn(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            raise ParseError
        user = authenticate(request,
                            username=username,
                            password=password,
                            )
        if user:
            login(request, user)
            # 1. 해당 함수를 호출하면 django는 user를 로그인 시킨다.
            # 2. 백엔드에서 user 정보가 담긴 session을 생성한다.
            # 3. 사용자에게 cookie를 보내준다.
            return Response({"welcome"})
        else:
            return Response({"error":"wrong password"})
        
class LogOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok":"bye"})
    
class PublicUser(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)

class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        if not old_password or not new_password:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)