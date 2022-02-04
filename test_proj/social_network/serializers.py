from rest_framework import serializers

from .models import UserModel,Post


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"

