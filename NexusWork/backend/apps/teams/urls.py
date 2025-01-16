#urls.py

from django.urls import path

from backend.apps.teams.views import TeamView, TeamViewDetail, TeamCreate


urlpatterns = [
    path('teams/', TeamView.as_view(), name='team_list'),
    path('team/<int:pk>/', TeamViewDetail.as_view(), name='current_team_detail'),
    path('team/create/', TeamCreate.as_view(), name='team_create'),

]

