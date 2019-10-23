from django.shortcuts import get_object_or_404

from rest_framework import generics

from stores.serializers import CategorySerializer, StoreSerializer
from stores.models import Category, Store


class StoreListAPI(generics.ListAPIView):
    serializer_class = StoreSerializer(many=True)

    def get_queryset(self):
        return Store.objects.all()
    
 
class StoreDetailAPI(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, self.kwargs['pk'])
        return obj
    


