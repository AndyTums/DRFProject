from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter

from config import settings
from users.apps import UsersConfig
from users.views import PaymentViewSet, UserViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register("payment", PaymentViewSet, basename="payment")
router.register("", UserViewSet, basename="users")

urlpatterns = []

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
