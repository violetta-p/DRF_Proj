from django.urls import path

from education.apps import EducationConfig
from rest_framework.routers import DefaultRouter

from education.views.course import CourseViewSet
from education.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView
from education.views.payment import PaymentListAPIView, create_payment, confirm_payment_intent, get_payment_info

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('create_payment/', create_payment),
    path('confirm_payment/', confirm_payment_intent),
    path('payment_info/', get_payment_info),

] + router.urls
