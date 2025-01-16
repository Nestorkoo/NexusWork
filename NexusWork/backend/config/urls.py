
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('backend.apps.customuser.urls')),
    path('api/v1/', include('backend.apps.spaces.urls')),
    path('api/v1/', include('backend.apps.teams.urls')),
    path('api/v1/', include('backend.apps.tasks.urls')),
    path('api/v1/', include('backend.apps.comments.urls')),
]
