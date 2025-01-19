#urls.py

from django.urls import path

from backend.apps.tasks.views import TasksCreate, TaskUpdate, TasksDelete, TasksList


urlpatterns = [
    path('tasks/list/<int:team_pk>/', TasksList.as_view(), name='task_list'),
    path('tasks/create/<int:team_pk>/', TasksCreate.as_view(), name='task_create'),
    path('tasks/update/<int:team_pk>/<int:task_pk>/', TaskUpdate.as_view(), name='task_update'),
    path('tasks/delete/<int:team_pk>/<int:task_pk>/', TasksDelete.as_view(), name='task_delete'),

]

