from django.urls import path

from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, UserPaymentListAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('user/payment/', UserPaymentListAPIView.as_view(), name='user_payment_list'),

] + router.urls
