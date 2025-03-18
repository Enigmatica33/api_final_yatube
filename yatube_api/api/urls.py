from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register('v1/posts', PostViewSet, basename='posts')
v1_router.register('v1/groups', GroupViewSet, basename='groups')
v1_router.register('v1/follow', FollowViewSet, basename='follows')
v1_router.register(
    r'v1/posts/(?P<post_id>.+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('', include(v1_router.urls)),
]
