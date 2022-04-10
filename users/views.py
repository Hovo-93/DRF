from django.contrib.auth.models import AbstractUser
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.serializers import UserModelSerializer,UserSerializerWithName
from rest_framework import mixins, viewsets, generics


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2


class UserCustomViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filterset_fields = ['uid']

    def get_serializer_class(self):
        if self.request.version == '2':
            return UserSerializerWithName
        return UserModelSerializer
