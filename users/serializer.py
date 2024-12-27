from rest_framework.serializers import ModelSerializer

from users.models import Payment, User, Subscription


class SubscriptionSerializer(ModelSerializer):
    """Serializer для модели SUBSCRIPTION"""

    class Meta:
        model = Subscription
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    """Serializer для модели PAYMENT"""

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):
    """Serializer для модели USER"""

    sub_list = SubscriptionSerializer(many=True, read_only=True, source='subscription_set')
    payment_list = PaymentSerializer(many=True, read_only=True, source='payment_set')

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'country', 'photo', 'sub_list', 'payment_list']
