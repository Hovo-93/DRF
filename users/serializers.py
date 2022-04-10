from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from users.models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('uid', 'username', 'first_name', 'last_name',)


class UserSerializerWithName(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_active',)
