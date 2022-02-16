from itertools import chain

from django.db.models import Count, Q
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from dateutil import parser

from .models import UserModel, Post, Like
from .serializers import UserModelSerializer, PostSerializer, LikeSerializer, LikeAmountByDaySerializer, \
    UserActivitySerializer


class CreateUserModelViewSet(CreateAPIView):
    serializer_class = UserModelSerializer
    permission_classes = (AllowAny, )


class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeViewSet(CreateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    http_method_names = ('post', 'delete', )

    @action(detail=False, http_method_names=('get', ))
    def analytics(self, request):
        """returns amount of likes per day by user."""
        queryset = Like.objects.filter(user=request.user)
        query_params = request.query_params
        date_from_str = query_params.get('date_from')
        date_to_str = query_params.get('date_to')

        if date_from := self.__parse_string_to_date(date_from_str):
            queryset = queryset.filter(created_at__gte=date_from)

        if date_to := self.__parse_string_to_date(date_to_str):
            queryset = queryset.filter(created_at__lte=date_to)

        queryset = queryset.values('created_at').annotate(likes_amount=Count('status', filter=Q(status=True)), dislikes_amount=Count('status', filter=Q(status=False)))
        serializer = LikeAmountByDaySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def __parse_string_to_date(self, date):
        """parses query params to date."""
        try:
            result_date = parser.parse(date).date()
        except TypeError:
            return None

        return result_date


class UserActivityRetrieveListViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserActivitySerializer
