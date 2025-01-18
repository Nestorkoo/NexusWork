#urls.py

from django.urls import path

from backend.apps.teams.views import TeamView, TeamViewDetail, TeamCreate, TeamLeaveView, TeamAddMemberView, TeamUpdateView


urlpatterns = [
    path('teams/', TeamView.as_view(), name='team_list'),
    path('team/<int:pk>/', TeamViewDetail.as_view(), name='current_team_detail'),
    path('team/create/', TeamCreate.as_view(), name='team_create'),
    path('team/delete/<int:pk>/', TeamViewDetail.as_view(), name='team_delete'),
    path('team/leave/<int:pk>/', TeamLeaveView.as_view(), name='team_leave'),
    path('team/join/<int:team_pk>/<int:user_pk>/', TeamAddMemberView.as_view(), name='team_join'),
    path('team/update/<int:pk>/', TeamUpdateView.as_view(), name='team_update'),
]

