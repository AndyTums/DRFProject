from rest_framework.serializers import ModelSerializer

from course.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """Serializer для модели COURSE"""

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    """Serializer для модели COURSE"""

    class Meta:
        model = Lesson
        fields = "__all__"
