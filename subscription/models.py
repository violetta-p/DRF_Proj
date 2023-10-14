from django.db import models

from education.models import Course
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Subscription(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', **NULLABLE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Is actual')

    def __str__(self):
        return f'{self.course_id}'

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
