from django.db import models
from django.urls import reverse
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):

    name = models.CharField(max_length=100, verbose_name='Course name')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    preview_pic = models.ImageField(upload_to='course_pictures/', **NULLABLE, verbose_name='Picture')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Creation date')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Lesson name')
    description = models.TextField(verbose_name='Description', **NULLABLE,)
    preview_pic = models.ImageField(upload_to='lesson_pictures/', **NULLABLE, verbose_name='Picture')
    url = models.URLField(max_length=1000, verbose_name='Url', **NULLABLE,)
    creation_date = models.DateField(auto_now_add=True, verbose_name='Creation date')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='Course', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


class Payment(models.Model):

    payment_options = [('cash', 'cash payment'),
                       ('card', 'transfer')]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User', **NULLABLE)
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='Course', **NULLABLE)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, verbose_name='Lesson', **NULLABLE)
    payment_sum = models.IntegerField(verbose_name='Sum')
    payment_method = models.CharField(max_length=30, choices=payment_options, default='transfer', verbose_name='Payment options')

    def __str__(self):
        return f'{self.user} - {self.lesson}'

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
