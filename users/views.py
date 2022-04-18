from django.contrib.auth.models import AbstractUser
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.serializers import UserModelSerializer
from rest_framework import mixins, viewsets, generics


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2


class UserCustomViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    # permission_classes = [IsAdminUser]
    queryset = User.objects.all().order_by('uid')
    serializer_class = UserModelSerializer
    filterset_fields = ['uid']
    pagination_class = LargeResultsSetPagination

    # def get_serializer_class(self):
    #     if self.request.version == '2':
    #         return UserSerializerWithName
    #     return UserModelSerializer
