import stripe
from rest_framework import status
from rest_framework.response import Response


def create_stripe_payment(payment, client):
    payment = stripe.PaymentIntent.create(
        amount=float(payment.payment_sum),
        currency='rub',
        payment_method_types=[payment.payment_method],
        receipt_email=str(client.email),
    )
    return Response(status=status.HTTP_200_OK, data=payment)


def get_stripe_payment(customer):
    payment_list = stripe.PaymentIntent.list(customer=customer.id, limit=10)
    last_payment = payment_list.get('data')[0]
    return last_payment
