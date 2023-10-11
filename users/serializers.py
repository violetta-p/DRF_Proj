from rest_framework import serializers

from education.models import Payment
from education.serializers.payment import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'phone', 'country', 'avatar')


class UserPaymentSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer
    class Meta:
        model = Payment
        fields = ('payment_date', 'lesson', 'course', 'payment_sum', 'payment_method')


class CommonUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'phone', 'country', 'avatar')
        