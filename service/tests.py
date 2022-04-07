import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
# from mixer.backend.django import mixer
# from django.contrib.auth.models import User
from users.views import UserCustomViewSet
from users.models import User
from to.views import ProjectModelViewSet, TodoModelViewSet
from to.models import Project, Todo


class TestUserCustomViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserCustomViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'last_name': 'Пушкин',
                                               'username': 'Pushkinian'}, format='json')
        view = UserCustomViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_detail(self):
        user = User.objects.create(first_name='Сэр Исаа́к Нью́то́н', username='apple')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@mail.com',
                                              'admin1111')

        client.login(username='admin', password='admin1111')

        response = client.put(f'/api/users/{user.uid}/', {'last_name': 'Сэр Исаа́к Нью́то́н', 'username': 'Neutron'},
                              fomat='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestProjectModelViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_edit_admin(self):
    #      user = User.objects.create(first_name='Сэр Исаа́к Нью́то́н', username='apple')
    #      project = Project.objects.create(title ='Emc',users = user)
    #      to =
    #      admin = User.objects.create_superuser('admin', 'admin@admin.com',
    #                                            'admin123456')
    #      self.client.login(username='admin', password='admin123456')
    #      response = self.client.put(f'/api/todos/{to.id}/', {'first_name': 'Руслан и Людмила', 'project': project.user.uid})
    #
    #      self.assertEqual(response.status_code, status.HTTP_200_OK)
