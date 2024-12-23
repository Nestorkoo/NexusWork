from rest_framework import serializers
from backend.apps.customuser.models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
    def create(self, valid_data):
        if len(valid_data['password']) < 6:
            raise serializers.ValidationError('the password should be at least 6 characters long')

        if 'email' not in valid_data:
            raise serializers.ValidationError('Please enter your email!')
        if 'first_name' not in valid_data:
            raise serializers.ValidationError('Please enter your first name')
        if 'last_name' not in valid_data:
            raise serializers.ValidationError('Please enter your last name')
        
        user = CustomUser(
            username=valid_data['username'],
            first_name=valid_data['first_name'],
            last_name=valid_data['last_name'],
            email=valid_data['email'],
        )
        user.set_password(valid_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            else:
                raise serializers.ValidationError('Invalid username or password')
        else:
            raise serializers.ValidationError('Must include both username and password')
        


        