from django.urls import path

from rest_framework.routers import DefaultRouter

from subscription.apps import SubscriptionConfig
from subscription.views import SubscriptionCreateAPIView, SubscriptionListAPIView, SubscriptionUpdateAPIView, SubscriptionDestroyAPIView

app_name = SubscriptionConfig.name

urlpatterns = [
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/', SubscriptionListAPIView.as_view(), name='subscription_list'),
    path('subscription/update/<int:pk>/', SubscriptionUpdateAPIView.as_view(), name='subscription_update'),
    path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),
]
