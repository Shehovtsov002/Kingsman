from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'}, required=True)
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'}, required=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES)
    gender = serializers.ChoiceField(choices=User.GENDER_CHOICES)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'gender', 'height', 'weight', 'password', 'password2',
                  'role']
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('Passwords do not match')
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        refresh = RefreshToken.for_user(user)
        return {
            'user': user,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
