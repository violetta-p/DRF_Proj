import json
from datetime import date

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


from education.models import Course, Lesson
from subscription.models import Subscription
from users.models import User

current_date = date.today().strftime("%Y-%m-%d")


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="Test@mail.ru",
            password="Test12345",
            is_active=True,
        )

        self.course = Course.objects.create(
            name='test_course'
        )

        self.lesson = Course.objects.create(
            name='test_sub',
        )

        self.subscription = Subscription.objects.create(
            course_id=self.course,
            user_id=self.user,
            is_active=True
        )


    def test_get_list(self):
        response = self.client.get(
            reverse('subscription:subscription_list')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        print(response.json())

    def test_create_subscription(self):
        data = {
            'user_id': self.user.pk,
            'course_id': self.course.pk,
            'is_active': True
        }

        response = self.client.post(
            reverse('subscription:subscription_create'),
            data=data)
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_subscription(self):
        data2 = {
            'user_id': self.user.pk,
            'course_id': self.course.pk,
            'is_active': False
        }
        response = self.client.put(
            reverse('subscription:subscription_update', kwargs={'pk': self.subscription.pk}),
            data=data2,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_subscription(self):
        response = self.client.delete(
            reverse('subscription:subscription_delete', kwargs={'pk': self.subscription.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

