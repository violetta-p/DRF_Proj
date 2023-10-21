from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from rest_framework.response import Response

import os
import stripe

from education.services import create_stripe_payment, get_stripe_payment
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

        create_stripe_payment(new_payment, self.request.user)


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def retrieve(self, request, *args, **kwargs):
        current_user = self.request.user
        instance = get_stripe_payment(current_user)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
