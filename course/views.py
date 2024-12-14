from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from course.models import Course, Lesson
from course.serializer import CourseSerializer, LessonSerializer

""" РАБОТА С МОДЕЛЬЮ COURSE """


class CourseViewSet(ModelViewSet):
    """ViewSet для модели COURSE"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


""" РАБОТА С МОДЕЛЬЮ LESSON """


class LessonCreateApiView(CreateAPIView):
    """Create для модели COURSE"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveApiView(RetrieveAPIView):
    """Retrieve для модели COURSE"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateApiView(UpdateAPIView):
    """Update для модели COURSE"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyApiView(DestroyAPIView):
    """Destroy для модели COURSE"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonListApiView(ListAPIView):
    """List для модели COURSE"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
