from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from backend.apps.spaces.serializers import SpaceSerializer, SpaceUpdateSerializer
from backend.apps.customuser.models import CustomUser
from backend.apps.spaces.models import Space

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class SpaceCreateView(generics.CreateAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        space = serializer.save(owner=request.user)

        if not space:
            return Response({'error': 'Failed to create Space'}, status=status.HTTP_400_BAD_REQUEST)

        space.members.add(request.user)

        return Response({'message': f'Space "{space.name}" created!'}, status=status.HTTP_201_CREATED)


class SpaceUpdateView(generics.UpdateAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceUpdateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        space = self.get_object()
        serializer = self.get_serializer(space, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': f'Space "{space.name}" updated!'}, status=status.HTTP_200_OK)

class SpaceDeleteView(generics.DestroyAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        space = self.get_object()
        space.delete()
        return Response(f'Space {space} deleted!', status=status.HTTP_200_OK)

class SpaceAddUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, space_pk, user_pk):
        space = Space.objects.filter(pk=space_pk, owner=request.user).first()
        user = CustomUser.objects.filter(pk=user_pk).first()
        if space and user:
            if space.members.filter(pk=user_pk).exists():
                return Response(f'User {user} already in space {space}!', status=status.HTTP_400_BAD_REQUEST)
            space.members.add(user)
            return Response(f'User {user} added to space {space}!', status=status.HTTP_200_OK)
            
        return Response('You are not the owner of this space or user does not exist', status=status.HTTP_400_BAD_REQUEST)
class SpaceLeaveView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        space = Space.objects.get(pk=pk)           
        space.members.remove(user)
        return Response(f'User {user} left space {space}!', status=status.HTTP_200_OK)
    

class SpaceDetailView(generics.RetrieveAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class SpaceDeleteMemberView(generics.DestroyAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, space_pk, user_pk):
        space = Space.objects.filter(pk=space_pk, owner=request.user).first()
        user = CustomUser.objects.filter(pk=user_pk).first()
        if space and user:
            space.members.remove(user)
            return Response(f'User {user} removed from space {space}!', status=status.HTTP_200_OK)
        elif user or space is None: 
            return Response('Space or user does not exist', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('You are not the owner of this space or user does not exist', status=status.HTTP_400_BAD_REQUEST)

