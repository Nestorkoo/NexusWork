from rest_framework import serializers
from backend.apps.tasks.models import Task
from backend.apps.teams.models import Team

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = 'title', 'description'
    
    
    def create(self, validated_data):
        team_pk = self.context.get('team_pk') 
        if not team_pk:
            raise serializers.ValidationError({'team_pk': 'Team primary key is required'})

        try:
            team = Team.objects.get(pk=team_pk)
        except Team.DoesNotExist:
            raise serializers.ValidationError({'team_pk': 'Invalid team ID'})

        task = Task.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            status='open',
            assigned_to=team,
            created_by=self.context['request'].user
        )

        team.tasks.add(task)

        return task 
    def delete(self, instance):
        instance.delete()
        return instance
class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description']
        extra_kwargs = {
            'title': {'required': False},
            'description': {'required': False},
        }
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
    
class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at']
