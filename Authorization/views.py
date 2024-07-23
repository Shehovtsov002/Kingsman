from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from serizalizers import UserRegistrationSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterUser(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.save()
        return Response({
            'user': UserRegistrationSerializer(user_data['user']).data,
            'refresh': user_data['refresh'],
            'access': user_data['access'],
        })
