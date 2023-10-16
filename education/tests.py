import json
import os
from datetime import date

from django.contrib.gis.geos import factory
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, force_authenticate
from django.urls import reverse


from education.models import Course, Lesson
from users.models import User

current_date = date.today().strftime("%Y-%m-%d")


class LessonTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = User.objects.create(
            email="Test@mail.ru",
            password="Test12345",
            is_active=True,
        )

        cls.course = Course.objects.create(
            name='test_course'
        )
        cls.lesson = Lesson.objects.create(
            name='test_lesson',
            course=cls.course,
            url=r'https://www.youtube.com/link'

        )

    def test_get_list(self):

        response = self.client.get(
            reverse('education:lesson_list')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        print(response.json())

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 1,
                        "name": "test_lesson",
                        "description": None,
                        "preview_pic": None,
                        "url": 'https://www.youtube.com/link',
                        "creation_date": current_date,
                        "course": 1,
                        "user": None

                    }
                ]
            }
        )

    def test_create_lesson(self):

        data = {
            'name': 'test2',
            'course': self.course.id,
            'url': 'https://www.youtube.com/link'

        }

        response = self.client.post(
            reverse('education:lesson_create'),
            data=data

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_lesson(self):
        data2 = {
            'name': 'test_updated',
            'url': 'https://www.youtube.com/new_link'
        }
        response = self.client.put(
            reverse('education:lesson_update', kwargs={'pk': self.lesson.pk}),
            data=data2,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson(self):
        response = self.client.delete(
            reverse('education:lesson_delete', kwargs={'pk': self.lesson.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
