from rest_framework import serializers
from backend.apps.comments.models import Comment
from backend.apps.teams.models import Team

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        team_pk = self.context.get('team_pk')
        if not team_pk:
            raise serializers.ValidationError({'team_pk': 'Team primary key is required'})
        
        try:
            team = Team.objects.get(pk=team_pk)
        except Team.DoesNotExist:
            raise serializers.ValidationError({'team_pk': 'Invalid team ID'})
        comment_create = Comment.objects.create(
            text=validated_data['text'],
            author=self.context['request'].user,
            team=team
        ) 
        
        team.comment.add(comment_create)
        
        return comment_create

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
