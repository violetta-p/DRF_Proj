from rest_framework.routers import DefaultRouter

from subscription.apps import SubscriptionConfig
from subscription.views import SubscriptionViewSet

app_name = SubscriptionConfig.name

router = DefaultRouter()
router.register(r'subscription', SubscriptionViewSet, basename='subscription')

urlpatterns = [
    ] + router.urls
