from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework import generics
from .serializers import UserSerializer
from feeds.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


import logging

logger = logging.getLogger(__name__)


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):

        try:
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                serializer.is_valid(raise_exception=True)
                user_instance = serializer.save()
                refresh = RefreshToken.for_user(
                    user_instance)  # generating the JWT token
                access_token = str(refresh.access_token)
                headers = self.get_success_headers(serializer.data)
                res = {"access_token": access_token}

                return Response(res, status=status.HTTP_201_CREATED, headers=headers)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error('An error occurred: %s', e, exc_info=True)