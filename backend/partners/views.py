from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser

from accounts.models import Partner
from stores.models import Store
from stores.serializers import StoreListSerializer, StoreDetailSerializer
from partners.models import BusinessRegistration, Feedback
from partners.serializers import (
    RegisterBusinessRegistration,
    FeedbackSerializer
)


class PartnerStoreListAPI(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreListSerializer

    def get_queryset(self):
        partner = Partner.objects.get(user=self.request.user)
        queryset = Store.objects.filter(partner=partner).all()
        return queryset


class PartnerStoreDetailAPI(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)         # 자기 자신만 가능한 권한도 추가해야됨
    serializer_class = StoreDetailSerializer

    def get_queryset(self):
        return Store.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['store_id'])
        return obj


class BusinessRegistrationAPI(generics.GenericAPIView):
    # parser_class = (MultiPartParser, FormParser, FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RegisterBusinessRegistration

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveCreateFeedbackAPI(generics.GenericAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Feedback.objects.filter(store_id=self.kwargs['store_id'])
        return queryset.order_by('-created_at')

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        if len(request.data['content']) < 1:
            body = {'message': '내용을 입력해주세요'}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        body = {'message': '피드백 작성 완료'}
        return Response(body, status=status.HTTP_201_CREATED)
    

class DeleteFeedbackAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['feedback_id'])
        return obj
