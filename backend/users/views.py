from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly)

from .pagination import CustomLimitPagination
from .permissions import IsOwnerOrReadOnly
from users.serializers import CustomUserSerializer

User = get_user_model()


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    pagination_class = CustomLimitPagination
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)

    def get_permissions(self):
        if self.request.path == '/api/users/me/':
            return IsAuthenticated(),
        return super().get_permissions()
