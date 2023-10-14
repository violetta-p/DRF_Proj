import json
from datetime import date

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


from education.models import Course, Lesson

current_date = date.today().strftime("%Y-%m-%d")


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        self.course = Course.objects.create(
            name='test_course'
        )
        self.lesson = Lesson.objects.create(
            name='test_lesson',
            course=self.course
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
                        "id": 2,
                        "name": "test_lesson",
                        "description": None,
                        "preview_pic": None,
                        "url": None,
                        "creation_date": current_date,
                        "course": 1,
                        "user": None

                    }
                ]
            }
        )

    def test_lesson_create(self):
        data = {
            'name': 'test2',
            'course': self.course.id

        }
        response = self.client.post(
            reverse('education:lesson_create'),
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_lesson(self):
        data2 = {
            'name': 'test_updated',
        }
        response = self.client.put(
            reverse('education:lesson_update', kwargs={'pk': self.lesson.pk}),
            data=data2,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_lesson(self):
        response = self.client.delete(
            reverse('lesson_delete', kwargs={'pk': self.lesson.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
