from django.http import JsonResponse

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer

# Create your views here.


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
