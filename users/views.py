from datetime import date

from django.http import JsonResponse
from rest_framework import generics, viewsets, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from education.models import Payment
from education.permissions import IsOwner
from users.serializers import UserSerializer, UserPaymentSerializer, CommonUserSerializer, LoginSerializer
from users.models import User

current_date = date.today().strftime("%Y-%m-%d")

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
        elif self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = CommonUserSerializer
        else:
            self.serializer_class = UserSerializer
        return self.serializer_class


class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        user = request.data.get('user', {})
        serializer = UserSerializer(user, data=request.data, partial=True)
        user_to_update = serializer.save()
        if serializer.is_valid():
            user_to_update.last_login = current_date
            user_to_update.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")
