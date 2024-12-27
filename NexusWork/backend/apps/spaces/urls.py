from django.urls import path

from backend.apps.spaces.views import SpaceCreateView, SpaceUpdateView, SpaceDeleteView, SpaceAddUserView, SpaceLeaveView, SpaceDetailView, SpaceDeleteMemberView

urlpatterns = [
    path('space/create/', SpaceCreateView.as_view(), name='space_create'),
    path('space/update/<int:pk>/',SpaceUpdateView.as_view(), name='space_update'),
    path('space/delete/<int:pk>/', SpaceDeleteView.as_view(), name='space_delete'),
    path('space/join/<int:space_pk>/<int:user_pk>/', SpaceAddUserView.as_view(), name='space_join'),
    path('space/delete_member/<int:space_pk>/<int:user_pk>/', SpaceDeleteMemberView.as_view(), name='space_delete_member'),
    path('space/leave/<int:pk>/', SpaceLeaveView.as_view(), name='space_leave'),
    path('space/<int:pk>/', SpaceDetailView.as_view(), name='space_detail'),
]
