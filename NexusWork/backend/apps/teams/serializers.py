from rest_framework import serializers
from backend.apps.teams.models import Team
from backend.apps.spaces.models import Space

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'description', 'members','created_at', 'updated_at']
    
    def create(self, validated_data):
        if 'name' in validated_data and len(validated_data['name']) == 4:
            raise serializers.ValidationError('The name should be at least 4 characters long')

        if 'description' in validated_data and len(validated_data['description']) < 10:
            raise serializers.ValidationError('The description should be at least 10 characters long')

        members = validated_data.pop('members', [])
        team = Team.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            owner_id=self.context['request'].user
        )
        team.members.add(self.context['request'].user)
        team.members.add(*members)
        space_team = Space.teams.through.objects.create(team=team, space=self.context['request'].user.spaces.first())
        space_team.save()
        

        return team


class TeamUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'description']
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
        }
    def update(self, instance, validated_data):
        if 'name' in validated_data:
            name = validated_data['name']
            if len(name) < 4:
                raise serializers.ValidationError({'name': 'The name should be at least 4 characters long'})
            instance.name = name

        if 'description' in validated_data:
            description = validated_data['description']
            if len(description) < 10:
                raise serializers.ValidationError({'description': 'The description should be at least 10 characters long'})
            instance.description = description

        instance.save()
        return instance