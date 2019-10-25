from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser

from partners.serializers import (
    PartnerStoresSerializer,
    RegisterBusinessRegistration
)
from partners.models import BusinessRegistration
from accounts.models import Partner
from stores.models import Store


class PartnerStoreListAPI(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PartnerStoresSerializer

    def get_queryset(self):
        partner = Partner.objects.get(user=self.request.user)
        queryset = Store.objects.filter(partner=partner).all()
        return queryset


class PartnerStoreDetailAPI(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)         # 자기 자신만 가능한 권한도 추가해야됨
    serializer_class = PartnerStoresSerializer

    def get_queryset(self):
        return Store.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj


class BusinessRegistrationAPI(generics.GenericAPIView):
    parser_class = (MultiPartParser, FormParser, FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RegisterBusinessRegistration

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
