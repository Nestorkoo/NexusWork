from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from backend.apps.teams.serializers import TeamSerializer, TeamUpdateSerializer
from backend.apps.teams.models import Team

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
        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_200_OK)
