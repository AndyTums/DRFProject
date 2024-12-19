from django.conf.urls.static import static
from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter

from config import settings
from users.apps import UsersConfig
from users.views import PaymentViewSet, UserViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", UserViewSet, basename="user")
router.register("payment", PaymentViewSet, basename="payment")

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
