
from django.urls import path, include
from backend.apps.customuser.views import *
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
]
