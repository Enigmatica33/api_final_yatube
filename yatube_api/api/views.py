from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from api.serializers import (
    PostSerializer,
    CommentSerializer,
    GroupSerializer,
    FollowSerializer
)
from api.permissions import IsAuthorOrReadOnly
from posts.models import Post, Group, Comment, Follow


class PostViewSet(viewsets.ModelViewSet):
    """Представление для объектов модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Авторизованный пользователь создает пост."""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Представление для объектов модели Comment."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def get_post(self):
        """Возвращает объект поста."""
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        """Возвращает кверисет c комментариями для поста."""
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        """Создает комментарий для поста."""
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление для объектов модели Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = LimitOffsetPagination


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Представление для объектов модели Follow."""
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Возвращает кверисет c подписками пользователя."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """Текущий пользователь создает подписку."""
        serializer.save(user=self.request.user)
