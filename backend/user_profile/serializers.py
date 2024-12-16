from .models import UserProfile

from rest_framework import serializers

class UserProfileSerializer:
    class Get(serializers.ModelSerializer):

       

        class Meta:
            model = UserProfile
            fields = [
                "id",
                "user",
                "email",
                "mobile_number",
                "role",
                "preferred_name",
                "full_name",
                "gender",
                "dob",
                "image",
                "description",
            ]
            ref_name = "UserProfileGet"

    # Create

    class Post(serializers.ModelSerializer):
        class Meta:
            model = UserProfile
            fields = [
                "id",
                "preferred_name",
                "full_name",
                "mobile_number",
                "dob",
                "gender",
                "image",
                "role",
                "description",
            ]
            ref_name = "UserProfileSerializerPost"

    class Update(serializers.ModelSerializer):
        class Meta:
            model = UserProfile
            fields = [
                "id",
                "preferred_name",
                "full_name",
                "gender",
                "dob",
                "image",
                "email",
                "mobile_number",
                "role",
                "description",
            ]
            ref_name = "UserProfileSerializerUpdate"
