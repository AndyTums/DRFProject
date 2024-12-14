from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from users.models import Payment, User
from users.serializer import PaymentSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    """ViewSet для модели USER"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filterset_fields = ('date', )


class PaymentViewSet(ModelViewSet):
    """ViewSet для модели PAYMENT"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['course', 'lesson', 'method']
    ordering_fields = ['date']

    # filterset_fields = ('course', 'lesson', 'method',)
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ('date', )
