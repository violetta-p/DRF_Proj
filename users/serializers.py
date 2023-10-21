from django.contrib.auth import authenticate
from rest_framework import serializers

from education.models import Payment
from education.serializers.payment import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'phone', 'country', 'avatar', 'last_login')


class UserPaymentSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer
    class Meta:
        model = Payment
        fields = ('payment_date', 'lesson', 'course', 'payment_sum', 'payment_method')


class CommonUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'phone', 'country', 'avatar')


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300)
    username = serializers.CharField(max_length=300, read_only=True)
    password = serializers.CharField(max_length=150, write_only=True)
    token = serializers.CharField(max_length=300, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            raise serializers.ValidationError('An email address is required to log in.')
        if password is None:
            raise serializers.ValidationError('A password is required to log in.')

        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )
        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated.')

        return {'email': user.email, 'username': user.username, 'token': user.token}

    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'token')


