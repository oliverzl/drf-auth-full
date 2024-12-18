from django.urls import include, path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # path("", views.getRoutes),
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
    path("create/", views.CustomUserCreateView.as_view()),
    path("login/", views.CustomTokenObtainPairView.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
