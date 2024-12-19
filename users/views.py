from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from users.models import Payment, User
from users.serializer import PaymentSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserViewSet(ModelViewSet):
    """ViewSet для модели USER"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """ Хэширование пароля при создании """

        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PaymentViewSet(ModelViewSet):
    """ViewSet для модели PAYMENT"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['course', 'lesson', 'method']
    ordering_fields = ['date']
