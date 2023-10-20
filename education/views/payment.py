from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from rest_framework.response import Response

import os
import stripe

from users.models import User
from education.models import Payment
from education.serializers.payment import PaymentSerializer

stripe.api_key = os.getenv('STRIPE_API_KEY')


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_method',)
    ordering_fields = ('payment_date',)
    permission_classes = [IsAuthenticated]


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        new_payment = serializer.save()
        new_payment.user = self.request.user
        new_payment.save()

        stripe.PaymentIntent.create(
            amount=float(new_payment.payment_sum),
            currency='rub',
            payment_method_types=[new_payment.payment_method],
            receipt_email=str(self.request.user.email),
        )


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def retrieve(self, request, *args, **kwargs):
        current_user = self.request.user
        data = stripe.Charge.list(customer=current_user.id, limit=10)
        last_payment = data.get('data')[0]

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)




# @api_view(['POST'])
# def create_payment(request):
#     payment = stripe.PaymentIntent.create(
#         amount=float(Payment.payment_sum),
#         currency='rub',
#         payment_method_types=[Payment.payment_method],
#         receipt_email=str(User.email),
#     )
#
#     return Response(status=status.HTTP_200_OK, data=payment)
#


