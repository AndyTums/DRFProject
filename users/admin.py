from django.contrib import admin

from users.models import Payment, User


@admin.register(Payment)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'user', 'amount', 'method', )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
