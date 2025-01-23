from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from backend.apps.comments.serializers import CommentSerializer
from backend.apps.comments.models import Comment

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class CommentViewDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get(self, request, pk):
        if Comment.objects.filter(team=pk).exists():
            comments = Comment.objects.filter(team=pk)
        else:
            return Response({'Comments does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class CommentCreate(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['team_pk'] = self.kwargs.get('team_pk')
        return context
class CommentDelete(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()