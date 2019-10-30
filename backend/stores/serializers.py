from rest_framework import serializers

from accounts.models import Partner, Client
from accounts.serializers.client_serializers import ClientSerializer
from stores.models import Category, Option, Store, ClientReview, PartnerFeedback
from menus.serializers import MenuSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('main_category', 'sub_category',)


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('name',)


class StoreByDistanceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    options = serializers.StringRelatedField(many=True)
    distance = serializers.SerializerMethodField('get_distance')
    # addr = serializers.SerializerMethodField('get_old_address')
    
    class Meta:
        model = Store
        fields = ('id', 'name', 'category', 'description', 'lon', 'lat', 'thumbnail', 'contact',
                  'road_addr', 'common_addr', 'addr', 'tags', 'price_avg', 'partner', 'review_cnt', 'view_cnt', 'options', 'distance')

    def get_distance(self, obj):
        return int(obj.distance.m)

    def get_old_address(self, obj):
        return f'{obj.common_addr} {obj.addr}'


class PartnerFeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartnerFeedback
        fields = '__all__'
        read_only_fields = ('id', 'store', 'review', 'partner', 'created_at')

    def create(self, validated_data):
        store_id = self.context.get('view').kwargs.get('store_id')
        if store_id is None:
            raise serializers.ValidationError("해당 Store가 존재하지 않습니다.")
        store = Store.objects.get(pk=store_id)
        
        review_id = self.context.get('view').kwargs.get('review_id')
        if review_id is None:
            raise serializers.ValidationError("해당 ClientReview가 존재하지 않습니다.")
        review = ClientReview.objects.get(pk=review_id)

        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            if user is None:
                raise serializers.ValidationError("존재하지 않는 User입니다.")
        partner = Partner.objects.get(user=user)

        feedback = PartnerFeedback.objects.create(
            store=store,
            review=review,
            partner=partner,
            content=validated_data['content']
        )
        return feedback


class ClientReviewSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    feedbacks = PartnerFeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = ClientReview
        fields = '__all__'
        read_only_fields = ('id', 'client', 'store', 'created_at')

    def create(self, validated_data):
        store_id = self.context.get('view').kwargs.get('store_id')
        if store_id is None:
            raise serializers.ValidationError("해당 Store가 존재하지 않습니다.")
        
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            if user is None:
                raise serializers.ValidationError("존재하지 않는 User입니다.")
        client = Client.objects.get(user=user)
        store = Store.objects.get(pk=store_id)
        review = ClientReview.objects.create(
            store=store,
            client=client,
            content=validated_data['content']
        )
        return review


class StoreListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Store
        fields = ('id', 'name', 'category', 'lon', 'lat', 'thumbnail', 'contact', 'road_addr',
                  'common_addr', 'addr', 'view_cnt',)


class StoreDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    options = serializers.StringRelatedField(many=True)
    reviews = ClientReviewSerializer(many=True, read_only=True)
    menus = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ('id', 'name', 'category', 'description', 'lon', 'lat', 'thumbnail', 'contact',
                  'road_addr', 'common_addr', 'addr', 'tags', 'price_avg', 'partner', 'review_cnt',
                  'view_cnt', 'menus', 'reviews', 'options')


