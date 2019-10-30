from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from clients.models import Review
from clients.serializers import ReviewSerializer


class RetrieveCreateClientReviewAPI(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.filter(store_id=self.kwargs['store_id'])
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
        body = {'message': '리뷰 작성 완료'}
        return Response(body, status=status.HTTP_201_CREATED)


class DeleteClientReivewAPI(generics.GenericAPIView):
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        obj = get_object_or_404(self.get_queryset(), id=kwargs['review_id'])
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)