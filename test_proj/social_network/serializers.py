from rest_framework import serializers

from .models import (
    UserModel,
    Post,
    Like,
    )


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username','password', 'first_name', 'last_name', 'email')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'text']


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = ('user', 'post')


class LikeAmountByDaySerializer(serializers.Serializer):
    date_created = serializers.DateField()
    likes_amount = serializers.IntegerField()


class UserActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'last_login', 'last_action')
