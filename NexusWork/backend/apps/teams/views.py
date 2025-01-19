from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from backend.apps.teams.serializers import TeamSerializer, TeamUpdateSerializer
from backend.apps.teams.models import Team
from backend.apps.customuser.models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class TeamView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamCreate(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamViewDetail(APIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if Team.objects.filter(pk=pk).exists():
            team = Team.objects.get(pk=pk)
        else:
            return Response({'Team does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        tasks = team.tasks.all()
        task_data = [{'id': task.id, 'name': task.title, 'description': task.description, 'status': task.status} for task in tasks]
        
        serializer = TeamSerializer(team)
        team_data = serializer.data
        team_data['tasks'] = task_data
        
        return Response(team_data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        if Team.objects.filter(pk=pk, owner_id=request.user).exists():
            team = Team.objects.get(pk=pk)
        else:
            return Response({'Team does not exist or you are not the owner'}, status=status.HTTP_400_BAD_REQUEST)
        team.delete()
        return Response(f'Team {team} deleted successfully', status=status.HTTP_200_OK)

    def post(self, request, pk):
        user = request.user
        team = Team.objects.get(pk=pk)
        team.members.remove(user)
        return Response(f"User {user} removed from team {team}", status=status.HTTP_200_OK)

class TeamAddMemberView(APIView):
    autherntication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    def post(self, request, team_pk, user_pk):
        team = Team.objects.filter(pk=team_pk, owner_id=request.user).first()
        user = CustomUser.objects.filter(pk=user_pk).first()
        if team and user:
            if team.members.filter(pk=user_pk).exists():
                return Response({'User already in team'}, status=status.HTTP_400_BAD_REQUEST)    
            team.members.add(user)
            return Response({'User added to team'}, status=status.HTTP_200_OK)
        return Response({'Team or user does not exist'}, status=status.HTTP_400_BAD_REQUEST)

class TeamLeaveView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        team = Team.objects.get(pk=pk)
        if not team or not user:
            return Response({'Team or user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        team.members.remove(user)
        return Response(f"User {user} leaved from team {team}", status=status.HTTP_200_OK)

class TeamUpdateView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()
    serializer_class = TeamUpdateSerializer


