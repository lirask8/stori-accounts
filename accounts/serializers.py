from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		exclude = (
			'created_at',
			'modified_at',
		)


class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		exclude = (
			'created_at',
			'password',
			'is_active',
			'modified_at',
		)
