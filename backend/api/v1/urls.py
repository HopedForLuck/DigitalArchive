from django.urls import include, path
from rest_framework import routers

from posts.views import PostViewSet, CommentViewSet, TagViewSet
from users.views import CustomUserViewSet

router = routers.DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('tags', TagViewSet, basename='tags')
router.register('comments', CommentViewSet, basename='comments')
router.register('users', CustomUserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
