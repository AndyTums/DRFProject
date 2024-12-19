from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """ Проверка авторизированно пользователя на нахождения в группе Moderator """

    message = 'У вас недостаточно прав!'

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Moderator").exists()


class IsOwner(permissions.BasePermission):
    """ Проверка является ли пользователь владельцем."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
