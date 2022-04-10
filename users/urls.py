from django.urls import path
from .views import UserCustomViewSet

app_name = 'users'

urlpatterns = [
    path('', UserCustomViewSet.as_view()),
]
