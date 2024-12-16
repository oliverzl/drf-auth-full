from django.urls import path
from user_profile.views import UserProfileView

urlpatterns = [
    path("list", UserProfileView.List.as_view()),
    path("<int:pk>", UserProfileView.Get.as_view()),
    path("create", UserProfileView.Create.as_view()),
    path("<int:pk>/update", UserProfileView.Update.as_view()),
    path("<int:pk>/delete", UserProfileView.Delete.as_view()),
]
