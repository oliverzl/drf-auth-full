from django.shortcuts import render
from rest_framework.response import Response
from django.http import Http404

from authapi.models import User
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from user_profile.models import UserProfile
from .serializers import UserProfileSerializer

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, OuterRef, ProtectedError, Subquery
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

User = get_user_model()


class UserProfileView:
    class UserProfileBaseView(generics.GenericAPIView):
        # permission_classes = [IsAuthenticated]
        # serializer_class = ProfileSerializer.Get
        queryset = UserProfile.objects.all()

    class List(UserProfileBaseView, generics.ListAPIView):
        permission_classes = [AllowAny]
        authentication_classes = []

        def get_queryset(self):
            queryset = super().get_queryset()

            return queryset

    class Get(UserProfileBaseView, generics.RetrieveAPIView):
        permission_classes = [AllowAny]
        authentication_classes = []
        serializer_class = UserProfileSerializer.Get

    class Create(UserProfileBaseView, generics.CreateAPIView):
        serializer_class = UserProfileSerializer.Post

        def post(self, request, *args, **kwargs):
            mutable_data = request.data.copy()

            print("mutable", mutable_data)
            serializer = self.serializer_class(data=mutable_data)
            if serializer.is_valid():
                # Save the UserProfile instance
                profile = serializer.save()

                # Create the User instance
                email = mutable_data.get("email")
                if not email:
                    return Response(
                        {"error": "Email is required to create a user."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                user = User.objects.create(email=email)

                # Link the User to the UserProfile
                profile.user = user
                profile.email = email  # Explicitly set the email field

                profile.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class Update(generics.UpdateAPIView):
        """
        Update a user profile.

        This endpoint allows for the update of a user profile.

        Request body should include profile-specific fields such as:
        - full_name: User's full name
        - preferred_name: User's preferred name
        - role: User's role in the system
        - school: ID of the school the user belongs to (if applicable)

        Returns:
        - 200 OK: Profile updated successfully
        - 400 Bad Request: Invalid data provided
        """

        permission_classes = [AllowAny]
        authentication_classes = []
        serializer_class = UserProfileSerializer.Update
        queryset = UserProfile.objects.all()

        def patch(self, request, *args, **kwargs):
            request.data._mutable = True

            if request.data.get("email"):
                request.data["email"] = request.data["email"].lower()

            request.data._mutable = False

            data = request.data.dict()
            print("START OF DATA AND RESPONSE")
            print(request.data)
            print("data: ", data)
            response = super().patch(request, *args, **kwargs)
            print(response)
            print("END OF DATA AND RESPONSE")
            if response.status_code == 200:
                user_profile_obj = UserProfile.objects.get(id=kwargs["pk"])
                print(user_profile_obj)

                # add children + teachers to the group
                reset_group_flag = True  # update this logic and test the groups!
                print("data: ", data)

                user_profile_obj.save()

            return response

    class Delete(UserProfileBaseView, generics.DestroyAPIView):
        """
        Delete a user profile.

        This endpoint allows for the deletion of a user profile.

        Returns:
        - 200 OK: Profile deleted successfully
        - 403 Forbidden: User does not have permission to delete the profile
        """

        permission_classes = [AllowAny]
        authentication_classes = []

        def delete(self, request, *args, **kwargs):
            try:
                profile_obj = UserProfile.objects.get(id=self.kwargs["pk"])
                user_obj = User.objects.get(email=profile_obj.user.email)
                super().delete(request, *args, **kwargs)
                user_obj.delete()
                return Response(status=status.HTTP_200_OK)
            except UserProfile.DoesNotExist:
                raise Http404("User profile not found.")
            except User.DoesNotExist:
                return Response(
                    {"error": "Associated user not found."}, status=status.HTTP_404_NOT_FOUND
                )
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    class DeleteBulk(UserProfileBaseView, generics.DestroyAPIView):
        permission_classes = [AllowAny]
        authentication_classes = []

        def delete(self, request, *args, **kwargs):
            ids = request.data.get("selectionModel")
            failed_ids = []
            for id in ids:
                try:
                    profile_obj = UserProfile.objects.get(id=id)
                    user_obj = User.objects.get(
                        email__iexact=profile_obj.email
                    )  # retrieve emails regardless of upper case
                    profile_obj.delete()
                    user_obj.delete()
                except (ObjectDoesNotExist, ProtectedError):
                    failed_ids.append(id)
            if len(failed_ids) == len(ids):
                response = Response(
                    {"status": "All Failed to delete", "failed_ids": failed_ids},
                    status=status.HTTP_403_FORBIDDEN,
                )

                return response
            elif failed_ids:
                response = Response(
                    {"status": "partial", "failed_ids": failed_ids},
                    status=status.HTTP_200_OK,
                )

                return response
            else:
                response = Response({"status": "success"}, status=status.HTTP_200_OK)

                return response
