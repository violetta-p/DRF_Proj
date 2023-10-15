import json
from datetime import date

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


from education.models import Course, Lesson
from subscription.models import Subscription

current_date = date.today().strftime("%Y-%m-%d")


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        self.lesson = Course.objects.create(
            name='test_sub',
        )

        self.course = Subscription.objects.create(
            course_id=1,
            user_id=self.user,
            is_active=True
        )


    def test_get_list(self):

        response = self.client.get(
            reverse('subscription:subscription')
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
                        "url": 'https://www.youtube.com/link',
                        "creation_date": current_date,
                        "course": 2,
                        "user": None

                    }
                ]
            }
        )


