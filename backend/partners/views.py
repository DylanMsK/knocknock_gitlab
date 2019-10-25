from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from partners.serializers import PartnerStoresSerializer
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