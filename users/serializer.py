from rest_framework.serializers import ModelSerializer

from users.models import Payment, User


class UserSerializer(ModelSerializer):
    """Serializer для модели USER"""

    class Meta:
        model = User
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    """Serializer для модели PAYMENT"""

    class Meta:
        model = Payment
        fields = "__all__"
