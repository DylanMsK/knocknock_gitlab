from django.shortcuts import get_object_or_404
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
from django.db.models import Q

from rest_framework import generics, status
from rest_framework.response import Response

from stores.serializers import CategorySerializer, StoreSerializer
from stores.models import Category, Store


class StoreListAPI(generics.ListAPIView):
    serializer_class = StoreSerializer

    def get_queryset(self):
        queryset = Store.objects.all()
        return queryset
    
    def filter_queryset(self, queryset):
        if self.request.query_params.get('name'):
            name = self.request.query_params.get('name')
            queryset = queryset.filter(Q(name__icontains=name))
        if self.request.query_params.get('loc')\
           and self.request.query_params.get('hour')\
           and self.request.query_params.get('d'):
            location = self.request.query_params.get('loc')
            lat, lon = map(float, location.split(','))
            pnt = GEOSGeometry(f'POINT({lat} {lon})', srid=4326)
            queryset = queryset.filter(Q(location__distance_lte=(pnt, 500)))
        return queryset


class StoreDetailAPI(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, self.kwargs['pk'])
        return obj
    