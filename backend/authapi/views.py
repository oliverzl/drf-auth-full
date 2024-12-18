from django.http import JsonResponse
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from django.db import transaction

from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserCreateSerializer, MyTokenObtainPairSerializer
from user_profile.models import UserProfile

User = get_user_model()


@api_view(["GET"])
def getRoutes(request):
    routes = ["/token", "/token/refresh"]

    return Response(routes)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):

        res = super().post(request, *args, **kwargs)
        user_id = res.data["id"]

        if user_id:
            # Update last login for the user
            user_profile_instance = UserProfile.objects.get(id=user_id)
            user_instance = user_profile_instance.user
            user_instance.last_login = timezone.now()
            user_instance.save()
        print("SIGNIN", res)
        return res


class CustomUserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
    def post(self, request):
        print("CREATION")
        print(request.data)
        mutable_data = request.data.copy()
        mutable_data["email"] = mutable_data["email"].lower()
        serializer = self.serializer_class(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            created_user = serializer.save()
            role = mutable_data.get("role", "NONE")
            UserProfile.objects.create(
                user=created_user, email=created_user.email, role=role
            )

            # send email
            

        return Response(serializer.data)