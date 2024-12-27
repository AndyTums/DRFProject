from rest_framework.serializers import ValidationError


def validate_youtube(value):
    """ Валидатор на проверку добавление видео только с хостинга YOUTUBE """

    if "youtube.com" not in value.lower():
        raise ValidationError("Видео должно быть загружено с видео-хостинга Youtube")
