from django.db import models
from django.urls import reverse
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):

    name = models.CharField(max_length=100, verbose_name='Course name')
    description = models.TextField(verbose_name='Description')
    preview_pic = models.ImageField(upload_to='course_pictures/', **NULLABLE, verbose_name='Picture')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Creation date')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Lesson name')
    description = models.TextField(verbose_name='Description')
    preview_pic = models.ImageField(upload_to='lesson_pictures/', **NULLABLE, verbose_name='Picture')
    url = models.URLField(max_length=1000, verbose_name='Url')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Creation date')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

