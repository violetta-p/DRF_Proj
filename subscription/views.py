from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]
