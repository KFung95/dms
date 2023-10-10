from rest_framework import permissions, status
from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import permissions, status
from django.shortcuts import render


def index(request):
    return render(request, "hello_world.html")


class UserRegister(APIView):
    # permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
