from django.core.management import BaseCommand

from course.models import Course
from users.models import User, Payment


class Command(BaseCommand):
    """ Команда для создания оплаты """

    def handle(self, *args, **options):
        user = User.objects.get(email="admin@gmail.com")
        course = Course.objects.get(title="Python")

        payment = Payment.objects.create(user=user, course=course, amount="20000",
                                         method="TRANSFER")
        payment.save()
