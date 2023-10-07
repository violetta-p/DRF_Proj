from django.core.management import BaseCommand
from django.core.management.color import no_style
from django.db import connection

from education.models import Payment, Lesson, Course


class Command(BaseCommand):
    Payment.objects.all().delete()
    Lesson.objects.all().delete()
    Course.objects.all().delete()

    sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Lesson, Course, Payment])
    with connection.cursor() as cursor:
        for sql in sequence_sql:
            cursor.execute(sql)

    def handle(self, *args, **options):

        courses = [
            {'name': 'Math', 'description': 'Collection of lessons in higher mathematics'},
            {'name': 'Languages', 'description': 'English, French, Spanish lessons'},
            {'name': 'IT', 'description': 'Basic course on python development'},
        ]

        lessons = [
            {'name': 'Integrals', 'description': 'Solving integral equations', 'course_id': 1},
            {'name': 'Articles', 'description': 'Articles in English(a, an, the)', 'course_id': 2},
            {'name': 'Python', 'description': 'Iterations (for, while)', 'course_id': 3},
        ]

        payments = [
            {'course_id': 1, 'payment_sum': 10000, 'payment_method': 'cash'},
            {'course_id': 2, 'payment_sum': 20000, 'payment_method': 'card'},
            {'course_id': 3, 'payment_sum': 150000, 'payment_method': 'card'},
            {'lesson_id': 1, 'payment_sum': 5500, 'payment_method': 'cash'},
            {'lesson_id': 2, 'payment_sum': 4000, 'payment_method': 'card'},
            {'lesson_id': 3, 'payment_sum': 1500, 'payment_method': 'card'},

        ]

        courses_for_DB = []

        for course in courses:
            courses_for_DB.append(Course(**course))

        Course.objects.bulk_create(courses_for_DB)

        lessons_for_DB = []
        for lesson in lessons:
            lessons_for_DB.append(Lesson(**lesson))

        Lesson.objects.bulk_create(lessons_for_DB)

        payments_for_DB = []
        for pay in payments:
            payments_for_DB.append(Payment(**pay))

        Payment.objects.bulk_create(payments_for_DB)

