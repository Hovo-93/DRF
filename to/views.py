from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from to.models import Project, Todo
from to.serializers import ProjectModelSerializer, TodoModelSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10


class MaxResultsSetPagination(PageNumberPagination):
    page_size = 20


# Create your views here.
class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_fields = ['title']
    pagination_class = LargeResultsSetPagination


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoModelSerializer
    filterset_fields = ['project']
    pagination_class = MaxResultsSetPagination

    def perform_destroy(self, instance):
        instance.status = 'CLS'
        instance.save()
