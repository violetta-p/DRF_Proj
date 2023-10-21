from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from education.models import Course
from education.paginators import CoursePaginator
from education.permissions import IsOwner, IsManager
from education.serializers.course import CourseSerializer
from subscription.tasks import send_message


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    #permission_classes = [IsAdminUser]
    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.user = self.request.user
        new_course.save()

    def perform_update(self, serializer):
        course = serializer.save()
        send_message(int(course.pk))

"""
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
"""