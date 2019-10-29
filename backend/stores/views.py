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
    StoreSerializer,
    StoreReviewSerializer,
    StoreSearchSerializer
)
from stores.models import Category, Store, Review


class StoreListAPI(generics.ListAPIView):
    serializer_class = StoreSerializer

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
        return queryset


class StoreDetailAPI(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSearchSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.kwargs['pk'])
        return obj


class CreateStoreReviewAPI(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StoreReviewSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data['content']) < 1:
            body = {'message': '내용을 입력해주세요'}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        body = {'message': '리뷰 작성 완료'}
        return Response(body, status=status.HTTP_201_CREATED)


class DeleteStoreReivewAPI(generics.GenericAPIView):
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        obj = get_object_or_404(queryset, id=kwargs['review_id'])
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

class SearchStoreAPI(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSearchSerializer

    def filter_queryset(self, queryset):
        if self.request.query_params.get('name'):
            name = self.request.query_params.get('name')
            queryset = queryset.filter(Q(name__icontains=name))
        return queryset