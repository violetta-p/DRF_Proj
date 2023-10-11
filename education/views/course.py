from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from education.models import Course
from education.permissions import IsOwner, IsManager
from education.serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        new_lesson = request.serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action in ('retrieve', 'update'):
            permission_classes = [IsAuthenticated, IsOwner | IsManager]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
