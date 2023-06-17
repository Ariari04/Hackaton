from rest_framework import serializers
from django.contrib.auth.models import User


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(required=False)

    def validate_phone_number(self, value):
        if not value:
            raise serializers.ValidationError("Phone number is required")
        return value

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        phone_number = validated_data.get('phone_number')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.phone_number = phone_number
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'phone_number')


# Change Password Serializer
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Invalid old password")
        return value

# from rest_framework import serializers
# from django.contrib.auth.models import User
#
#
# # User Serializer
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')
#
#
# # Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     phone_number = serializers.CharField(required=False)
#
#     def validate_phone_number(self, value):
#         if not value:
#             raise serializers.ValidationError("Phone number is required")
#         return value
#
#     def create(self, validated_data):
#         username = validated_data.get('username')
#         email = validated_data.get('email')
#         password = validated_data.get('password')
#         phone_number = validated_data.get('phone_number')
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.phone_number = phone_number
#         user.save()
#         return user
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password', 'phone_number')
#
#
# # Change Password Serializer
# class ChangePasswordSerializer(serializers.Serializer):
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)
#
#     def validate_old_password(self, value):
#         user = self.context['request'].user
#         if not user.check_password(value):
#             raise serializers.ValidationError("Invalid old password")
#         return value

# from rest_framework import serializers
# from django.contrib.auth.models import User
#
#
# # User Serializer
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')
#
#
# # Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password', 'phone_number')
#         extra_kwargs = {'password': {'write_only': True}}
#
#         def validate_number(self, value):
#             if not value:
#                 raise serializers.ValidationError("NOT")
#             return value
#
#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
#         return user
#
#
# # Change Password
#
# class ChangePasswordSerializer(serializers.Serializer):
#     model = User
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)
