from to.models import Project, Todo
from rest_framework.serializers import ModelSerializer
from users.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    # users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = Todo
        fields = '__all__'
