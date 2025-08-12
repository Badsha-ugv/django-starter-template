from rest_framework import serializers

from .models import (
    User,
    Profile
)


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
        except Exception as e:
            raise serializers.ValidationError(e)
        return user
