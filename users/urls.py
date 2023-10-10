from django.urls import path

from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, UserPaymentListAPIView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('user/payment/', UserPaymentListAPIView.as_view(), name='user_payment_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

] + router.urls
