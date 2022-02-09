from rest_framework import viewsets
from vote.views import VoteMixin

from .models import UserModel, Post
from .serializers import UserModelSerializer, PostSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class PostViewSet(viewsets.ModelViewSet, VoteMixin):
# class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
