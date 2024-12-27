from django.contrib import admin

from course.models import Course, Lesson


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'owner')


@admin.register(Lesson)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'owner', 'course')
