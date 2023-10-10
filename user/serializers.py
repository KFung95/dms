from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, data):
        user_obj = UserModel.objects.create_user(
            email=data["email"], password=data["password"]
        )
        user_obj.username = data["username"]
        user_obj.save()
        return user_obj

    def check_user(self, data):
        user = authenticate(username=data["email"], password=data["password"])
        if not user:
            raise ValidationError("User not found.")
        return user

    def get_email(self, data):
        user = self.check_user(data)
        if user:
            return user.email
