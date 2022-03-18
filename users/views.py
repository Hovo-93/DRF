from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.serializers import UserModelSerializer
from rest_framework import mixins, viewsets


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2


class UserCustomViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filterset_fields = ['uid']
    pagination_class = LargeResultsSetPagination

# Create your views here.
# class UserModelViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
