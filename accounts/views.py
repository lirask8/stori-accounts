# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from accounts.models import User

from common.utils import CommonMixin
from accounts.auth import authenticate, create_token
from accounts.permissions import AllowAny, IsAuthenticated
from accounts.serializers import (
    UserSerializer,
    ProfileSerializer,
)


class SignupAPIView(APIView, CommonMixin):
    permission_classes = (AllowAny,)

    def post(self, request):

        data = request.data
        response_data = {}
        response_data["success"] = True

        # TODO: Use a serializer
        if not 'email' in data:
            response_data["message"] = _("email is required ")
            response_data["success"] = False
            return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)

        user_exists = self.getObjectOrNone(User, email=data["email"])

        if user_exists is not None:
            response_data["success"] = False
            response_data["message"] = _("Email already in use")
            return Response(data=response_data, status=status.HTTP_206_PARTIAL_CONTENT)

        serializer = UserSerializer(data=data, many=False)

        if not serializer.is_valid():
            response_data["success"] = False
            response_data["message"] = self.returnSerializerErrors(serializer.errors)
            return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)

        created_user = serializer.save()
        response_data = ProfileSerializer(created_user, many=False).data

        return Response(data=response_data, status=status.HTTP_201_CREATED)


class SigninAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):

        data = request.data
        response_data = {}
        response_data["success"] = False

        # TODO: Use a serializer
        if not 'email' in data:
            response_data["message"] = _("email is required ")
            return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)
        if not 'password' in data:
            response_data["message"] = _("password is required ")
            return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=data["email"], password=data["password"])

        if user is None:
            response_data["message"] = _("Invalid user  or wrong credentials")
            return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)

        response_data["success"] = True
        response_data["token"] = create_token(user)

        return Response(data=response_data, status=status.HTTP_200_OK)


class ProfileAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        response_data = ProfileSerializer(request.user, many=False).data

        return Response(data=response_data, status=status.HTTP_200_OK)
