from datetime import timedelta
from time import strftime

from django.utils import timezone
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from course.models import Course, Lesson
from course.paginations import CustomPagination
from course.serializer import CourseSerializer, LessonSerializer, CourseDetailSerializer
from course.tasks import send_email
from users.permissions import IsModer, IsOwner

""" РАБОТА С МОДЕЛЬЮ COURSE """


class CourseViewSet(ModelViewSet):
    """ViewSet для модели COURSE"""

    queryset = Course.objects.all()
    pagination_class = CustomPagination

    def get_serializer_class(self):
        """ Обработка запроса вывода списка всех курсов или детальное отображение одного """

        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        """ Заполнение обьекта owner авторизованным пользователем """

        course = serializer.save(owner=self.request.user)
        course.save()

    def get_permissions(self):
        """ Запрет на удаление и добавление пользователю из группы Модераторов, разрешение на весь CRUD для
                                    авторизованного пользователя своих COURSE """

        if self.action == "create":
            self.permission_classes = (~IsModer,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (IsOwner | ~IsModer,)
        return super().get_permissions()

    def perform_update(self, serializer):
        """ После успешного изменения модуля COURSE и если он не обновлялся более 4 часов - отправляем
                                уведомление на почту всем подписчикам  """

        course = serializer.save()
        if timezone.now() - course.updated_at > timedelta(hours=4):
            subs = [sub.user.email for sub in course.subscribes.all()]
            send_email.delay(subs)
        else:
            print(f"Обновление было меньше чем 4 часа назад, отправки писем - не будет!")


""" РАБОТА С МОДЕЛЬЮ LESSON """


class LessonCreateApiView(CreateAPIView):
    """Create для модели COURSE"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        """ Заполнение обьекта owner авторизованным пользователем """

        lesson = serializer.save(owner=self.request.user)
        lesson.save()


class LessonRetrieveApiView(RetrieveAPIView):
    """Retrieve для модели COURSE"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsModer)


class LessonUpdateApiView(UpdateAPIView):
    """Update для модели COURSE"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsModer,)


class LessonDestroyApiView(DestroyAPIView):
    """Destroy для модели COURSE"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | ~IsModer,)


class LessonListApiView(ListAPIView):
    """List для модели COURSE"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination
