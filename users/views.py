from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from education.models import Payment
from education.serializers.payment import PaymentSerializer
from users.serializers import UserSerializer, UserPaymentSerializer
from users.models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserPaymentListAPIView(generics.ListAPIView):
    serializer_class = UserPaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ('payment_date',)