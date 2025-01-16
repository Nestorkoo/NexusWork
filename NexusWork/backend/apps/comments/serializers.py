from rest_framework import serializers
from backend.apps.comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        comment = Comment.objects.create(
            text=validated_data['text'],
            author=self.context['request'].user,
            team=self.context['request'].user.teams.first()
        )   

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
