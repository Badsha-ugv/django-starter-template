from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import (
    UserCreateSerializer
)
User = get_user_model()
