from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from menus.models import Menu
from menus.serializers import MenuSerializer


class RetrieveCreateMenuAPI(generics.GenericAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Menu.objects.filter(store_id=self.kwargs['store_id'])
        return queryset.order_by('id')

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        body = {'message': '메뉴 등록 완료', 'data': serializer.data}
        return Response(body, status=status.HTTP_201_CREATED)
    

class RetrieveUpdateDeleteMenuAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['menu_id'])
        return obj