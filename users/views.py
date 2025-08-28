from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerializer


class RegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user
    def validate_yosh(self, value):
        if value.yosh <= 19:
            raise serializers.ValidationError(
                "Yoshingiz mos kelmaydi"
            )
        return value