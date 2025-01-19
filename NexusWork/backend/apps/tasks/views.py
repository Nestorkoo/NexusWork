from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from backend.apps.teams.models import Team
from backend.apps.tasks.serializers import TaskSerializer, TaskUpdateSerializer, TaskListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from backend.apps.customuser.models import CustomUser
from backend.apps.tasks.models import Task

class TasksList(generics.ListCreateAPIView):
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        team_pk = self.kwargs['team_pk']
        return Team.objects.get(pk=team_pk).tasks.all()
class TasksCreate(generics.CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        team_pk = self.kwargs['team_pk']
        return Team.objects.get(pk=team_pk).tasks.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['team_pk'] = self.kwargs['team_pk']  # Передаємо team_pk у контекст
        return context

class TaskUpdate(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()
    
    def put(self, request, team_pk, task_pk):
        team = Team.objects.get(pk=team_pk)
        task = Task.objects.get(pk=task_pk)
        serializer = TaskUpdateSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TasksDelete(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()
    
    def delete(self, request, team_pk, task_pk):
        team = Team.objects.get(pk=team_pk)
        task = Task.objects.get(pk=task_pk)
        team.tasks.remove(task)

        return Response(f"Task {task} was delete successfully",status=status.HTTP_204_NO_CONTENT)