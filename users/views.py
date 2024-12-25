from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from course.models import Course
from users.models import Payment, User, Subscription
from users.serializer import PaymentSerializer, UserSerializer, SubscriptionSerializer
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


class SubscriptionViewSet(ModelViewSet):
    """ViewSet для модели SUBSCRIPTION"""

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['course', 'user']
    ordering_fields = ['date']

    def create(self, *args, **kwargs):
        """ Проверка наличие подписки у данного пользователя по ID COURSE """

        user = self.request.user  # Получаем пользователя запроса
        course = self.request.data.get('course')  # Получаем переданный курс

        course_item = get_object_or_404(Course, id=course)  # Проверяем есть ли данный курс в БД

        subs_item = Subscription.objects.filter(user=user, course=course_item)  # Фильтруем подписки пользователя

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка удалена'
            # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'Подписка добавлена'
            # Возвращаем ответ в API
        return Response({"message": message})
