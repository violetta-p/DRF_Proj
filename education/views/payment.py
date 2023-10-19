from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from education.models import Payment
from education.serializers.payment import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_method',)
    ordering_fields = ('payment_date',)
    permission_classes = [IsAuthenticated]

import os

import stripe
from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from education.models import Payment
from users.models import User

stripe.api_key = os.getenv('STRIPE_API_KEY')


@api_view(['POST'])
def create_payment(request):
    payment = stripe.PaymentIntent.create(
        amount=float(Payment.payment_sum),
        currency='rub',
        payment_method_types=[Payment.payment_method],
        receipt_email=str(User.email),
    )

    return Response(status=status.HTTP_200_OK, data=payment)


@api_view(['POST'])
def confirm_payment_intent(request):
    data = request.data
    payment_intent_id = data['payment_intent_id']

    stripe.PaymentIntent.confirm(payment_intent_id)

    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_payment_info(request):
    data = Payment.objects.last()
    last_payment_id = data['id']
    stripe.PaymentIntent.retrieve(last_payment_id)

