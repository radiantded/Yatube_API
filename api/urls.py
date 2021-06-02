from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers

from .views import CommentsViewSet, PostsViewSet, FollowViewSet, GroupViewSet


router_v1 = routers.DefaultRouter()
router_v1.register('v1/posts',
                   PostsViewSet,
                   basename='api_posts')
router_v1.register(r'v1/posts/(?P<post_id>\d+)/comments',
                   CommentsViewSet,
                   basename='api_comments')
router_v1.register('v1/follow',
                   FollowViewSet,
                   basename='api_follow')
router_v1.register('v1/group',
                   GroupViewSet,
                   basename='api_group')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router_v1.urls)),
]
