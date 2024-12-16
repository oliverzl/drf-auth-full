from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authapi/', include('authapi.urls')),
    path('user_profile/', include('user_profile.urls'))
]
