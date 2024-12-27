from rest_framework import serializers
from backend.apps.spaces.models import Space
from backend.apps.customuser.models import CustomUser


class SpaceSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(
        many=True, queryset=CustomUser.objects.all(), required=False
    )
    class Meta:
        model = Space
        fields = ['name', 'description', 'members', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        if len(validated_data['name']) < 4:
            raise serializers.ValidationError('The name should be at least 4 characters long')
        if len(validated_data['description']) < 10:
            raise serializers.ValidationError('The description should be at least 10 characters long')

        members = validated_data.pop('members', [])

        space = Space.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            owner=self.context['request'].user
        )

        space.members.add(self.context['request'].user) 
        space.members.add(*members)

        self.context['request'].user.spaces_count += 1
        self.context['request'].user.save()

        return space

    def update(self, instance, validated_data):
    # Оновлення полів: name та description
        for field in ['name', 'description']:
            if field in validated_data:
                value = validated_data[field]
                if field == 'name' and len(value) < 4:
                    raise serializers.ValidationError('The name should be at least 4 characters long')
                if field == 'description' and len(value) < 10:
                    raise serializers.ValidationError('The description should be at least 10 characters long')
                setattr(instance, field, value) 

        if 'members' in validated_data:
            members = validated_data.pop('members', [])
            instance.members.set(members)  
            instance.members.add(self.context['request'].user)  

        instance.save()
        return instance
    
class SpaceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = ['name', 'description']
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
        }

    def update(self, instance, validated_data):
        if 'name' in validated_data:
            name = validated_data['name']
            if len(name) < 4:
                raise serializers.ValidationError(
                    {'name': 'The name should be at least 4 characters long'}
                )
            instance.name = name

        if 'description' in validated_data:
            description = validated_data['description']
            if len(description) < 10:
                raise serializers.ValidationError(
                    {'description': 'The description should be at least 10 characters long'}
                )
            instance.description = description

        instance.save()
        return instance

