from rest_framework import serializers
from education.models import Lesson
from education.validators import URLValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [URLValidator(field='url')]
