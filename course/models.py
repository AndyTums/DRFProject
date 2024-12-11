from django.db import models


class Course(models.Model):
    """Модель: Курса"""

    title = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(
        upload_to="course/photo/", blank=True, null=True, verbose_name="Картинка"
    )

    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """Модель: Урока"""

    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="course/photo/", blank=True, null=True, verbose_name="Картинка"
    )

    video = models.FileField(upload_to="course/video/", null=True, blank=True)
    course = models.ForeignKey(
        Course, verbose_name="Курс", on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title
