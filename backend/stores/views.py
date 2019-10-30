from django.shortcuts import get_object_or_404
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.db.models import Q

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from stores.serializers import (
    CategorySerializer,
    StoreByDistanceSerializer,
    StoreListSerializer,
    StoreDetailSerializer
)
from stores.models import Category, Store


class StoreByDistanceListAPI(generics.ListAPIView):
    serializer_class = StoreByDistanceSerializer

    def get_queryset(self):
        location = self.request.query_params.get('loc')
        lat, lon = map(float, location.split(','))
        pnt = GEOSGeometry(f'POINT({lat} {lon})', srid=4326)
        queryset = Store.objects.annotate(distance=Distance('location', pnt))
        return queryset
    
    def filter_queryset(self, queryset):
        if self.request.query_params.get('hour')\
           and self.request.query_params.get('d'):
            hour = self.request.query_params.get('hour')
            distance = self.request.query_params.get('d')
            queryset = queryset.filter(Q(distance__lte=int(distance))).order_by('distance')
        return queryset[:100]


class StoreListAPI(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer

    def get_queryset(self):
        queryset = Store.objects.all()
        return queryset

    def filter_queryset(self, queryset):
        if self.request.query_params.get('name'):
            name = self.request.query_params.get('name')
            queryset = queryset.filter(Q(name__icontains=name))
        return queryset[:100]


class StoreDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.kwargs['store_id'])
        return obj
