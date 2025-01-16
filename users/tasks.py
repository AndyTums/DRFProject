from datetime import timedelta
from django.db.models import Q

from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def check_is_active():
    """ Проверка на активность пользователя, если заходил более месяца назад, вообще не заходил - делаем неактивным """

    month_ago = timezone.now() - timedelta(days=30)
    users_list = User.objects.filter(Q(last_login__isnull=True) | Q(last_login__lt=month_ago), is_active=True)

    if users_list:
        for user in users_list:
            user.is_active = False
            user.save()
            print(f"Статуc пользователя {user.email} изменен на {user.is_active}")

    print("Все пользователи исправлены!")
