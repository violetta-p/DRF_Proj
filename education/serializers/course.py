from rest_framework import serializers

from education.models import Course, Lesson
from subscription.models import Subscription


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()
    current_user = serializers.SerializerMethodField('_user')
    is_auth_user_active = serializers.SerializerMethodField()

    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user

    @staticmethod
    def get_is_auth_user_active(course):
        if Subscription.objects.filter(course_id=course.pk, is_active=True) is not None:
            return True
        return False

    @ staticmethod
    def get_lessons_count(course):
        return Lesson.objects.filter(course=course.pk).count()

    @staticmethod
    def get_lessons(course):
        return [course.name for course in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = ('name', 'lessons_count', 'lessons', 'current_user', 'is_auth_user_active')
