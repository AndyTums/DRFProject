from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from course.models import Course, Lesson


class User(AbstractUser):
    """Модель: Пользователь"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")

    first_name = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Фамилия"
    )
    phone = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="Телефон"
    )
    country = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Страна"
    )
    photo = models.ImageField(
        upload_to="users/avatars/", blank=True, null=True, verbose_name="Фото"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    """Модель: Пользователь"""

    METHOD_CHOICE = [('CASH', 'Наличные'),
                     ('TRANSFER', 'Перевод')]

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now,
                                max_length=30, blank=True, null=True, verbose_name="Дата и время оплаты")
    course = models.ForeignKey(Course, blank=True, null=True, verbose_name="Оплаченный курс", on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, blank=True, null=True, verbose_name="Оплаченный урок", on_delete=models.CASCADE)

    amount = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    method = models.CharField(default='TRANSFER', max_length=10, choices=METHOD_CHOICE, verbose_name="Метод оплаты")

    def __str__(self):
        return f'{self.user} - {self.course or self.lesson}'
