from django.conf.urls.static import static
from django.urls import path
from rest_framework.routers import SimpleRouter

from config import settings
from course.apps import CourseConfig
from course.views import (CourseViewSet, LessonCreateApiView,
                          LessonDestroyApiView, LessonListApiView,
                          LessonRetrieveApiView, LessonUpdateApiView)

app_name = CourseConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lessons_retrieve"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lessons_create"),
    path(
        "lessons/delete/<int:pk>/",
        LessonDestroyApiView.as_view(),
        name="lessons_delete"),
    path("lessons/update/<int:pk>/", LessonUpdateApiView.as_view(), name="lessons_update"),

]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
