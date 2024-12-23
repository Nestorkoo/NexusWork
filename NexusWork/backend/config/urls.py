
from django.contrib import admin
from django.urls import path, include

default_url = 'api/v1/my_spaces/<int:pk>/'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('backend.apps.customuser.urls')),
]
