from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


@shared_task
def send_email(subs):
    try:
        send_mail(subject="Изменение в курсе", message="Зайдите посмотрите, у нас что-то новенькое!",
                  from_email=EMAIL_HOST_USER, recipient_list=subs)
        print(f"Все письма направлены на Email{subs}")
    except Exception as e:
        print(f"Письмо на почту - НЕ ДОСТАВЛЕНО! Ошибка: {e}")
