from celery import shared_task

from config import settings
from django.core.mail import send_mail

from education.models import Course
from subscription.models import Subscription
from users.models import User


@shared_task
def send_message(course_pk):
    course = Course.objects.get(pk=course_pk)

    for subscription in Subscription.objects.filter(course_id=course_pk, is_active=True):
        user_id = int(subscription.user_id)
        user = User.objects.get(pk=user_id)
        user_email = user.email

        try:
            send_mail(
                subject=f'Update!',
                message=f'The {course.name} course has been updated!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user_email]
            )

        except Exception:
            raise Exception # Можно (потом) реализовать отправку сообщения об ошибке админу или запись ошибок в лог
