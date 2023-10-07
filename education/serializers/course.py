from rest_framework import serializers

from education.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('name', 'lessons_count', 'lessons')

    @staticmethod
    def get_lessons_count(course):
        return Lesson.objects.filter(course=course.pk).count()

    @staticmethod
    def get_lessons(course):
        return [course.name for course in Lesson.objects.filter(course=course)]
