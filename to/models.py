from django.db import models
from users.models import User


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField(max_length=200, blank=True)
    users = models.ManyToManyField(User)


class Todo(models.Model):
    ACTIVE = 'ACT'
    CLOSED = 'CLS'
    STATUSES = (
        (ACTIVE, ' активно'),
        (CLOSED, 'закрыто'),

    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE,max_length=128)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUSES, blank=True, default=ACTIVE,max_length=3)
