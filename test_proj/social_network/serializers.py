from rest_framework import serializers

from .models import UserModel,Post


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault(),
    # )
    # user = serializers.CharField(default=serializers.CurrentUserDefault())
    vote_score = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'text', 'vote_score']
