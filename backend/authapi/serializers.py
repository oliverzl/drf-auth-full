from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()  # Retrieve custom user model


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username
        # ...

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["id"] = self.user.profile.id  # Add user ID to response
        return data


class UserCreateSerializer(UserCreateSerializer):
    tokens = serializers.SerializerMethodField()
    profile_id = serializers.SerializerMethodField()

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "email",
            "password",
            "tokens",
            "profile_id",
        ]
        read_only_fields = ("created_at", "updated_at")
        ref_name = "UserCreate"

    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)
        refresh = str(tokens)
        access = str(tokens.access_token)
        data = {"refresh": refresh, "access": access}
        return data

    def get_profile_id(self, user):
        profile = user.profile
        return profile.id
