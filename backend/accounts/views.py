from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from accounts.models import Client, Partner
from accounts.serializers import (
    ClientSignupSerializer,
    PartnerSignupSerializer,
    LoginSerializer,
    # PartnerLoginSerializer,
    UserSerializer,
    ClientSerializer,
    PartnerSerializer
)
from knox.models import AuthToken


class ClientSignupAPI(generics.GenericAPIView):
    serializer_class = ClientSignupSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data['username']) < 6:       # 아이디 유효성 검사
            body = {'message': '아이디는 6자 이상으로'}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        if len(request.data['password']) < 6:       # 비밀번호 유효성 검사
            body = {'message': '비밀번호는 6자 이상으로'}   
            return Response(body, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        body = {'message': '회원가입 완료'}
        return Response(body, status=status.HTTP_201_CREATED)


class PartnerSignupAPI(generics.GenericAPIView):
    serializer_class = PartnerSignupSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data['username']) < 6:       # 아이디 유효성 검사
            body = {'message': '아이디는 6자 이상으로'}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        if len(request.data['password']) < 6:       # 비밀번호 유효성 검사
            body = {'message': '비밀번호는 6자 이상으로'}   
            return Response(body, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        body = {'message': '회원가입 완료'}
        return Response(body, status=status.HTTP_201_CREATED)


class ClientLoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        client = get_object_or_404(client, user=user)
        return Response(
            {
                "client": ClientSerializer(client, context=self.get_serializer_context()).data,
                "user": {
                    "username": user.username,
                    "token": AuthToken.objects.create(user)[1],
                }
            }
        )


class PartnerLoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        partner = get_object_or_404(Partner, user=user)
        return Response(
            {
                "partner": PartnerSerializer(partner, context=self.get_serializer_context()).data,
                "user": {
                    "username": user.username,
                    "token": AuthToken.objects.create(user)[1],
                }
            }
        )