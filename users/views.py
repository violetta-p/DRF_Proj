from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from education.models import Payment
from education.permissions import IsOwner
from users.serializers import UserSerializer, UserPaymentSerializer, CommonUserSerializer
from users.models import User


class UserPaymentListAPIView(generics.ListAPIView):
    serializer_class = UserPaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ('payment_date',)
    permission_classes = [IsOwner]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CommonUserSerializer

    def get_permissions_class(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = CommonUserSerializer
        else:
            self.serializer_class = UserSerializer
        return self.serializer_class
