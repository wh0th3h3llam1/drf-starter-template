from rest_framework import serializers

from core.serializers import DynamicFieldsModelSerializer

from users.models import User

# Create your serializers here.


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = (
            "username", "email",
            "first_name", "last_name",
        )
