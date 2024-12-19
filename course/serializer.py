from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from course.models import Course, Lesson


#     Работа с моделью COURSE
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


#
class CourseDetailSerializer(ModelSerializer):
    """ Отображение детальной информации по курсу + поле количество уроков в данном курсе """

    count_lessons = SerializerMethodField()
    lessons_list = LessonSerializer(many=True, read_only=True, source='lesson_set')

    def get_count_lessons(self, course):
        """ Метод добавляющий количество уроков в курсе """

        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'count_lessons', 'lessons_list',)
