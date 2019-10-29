from rest_framework import serializers

from accounts.models import Partner, Client
from stores.models import Category, Option, Store, ClientReview, PartnerFeedback


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('main_category', 'sub_category',)


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('name',)


class StoreSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    options = serializers.StringRelatedField(many=True)
    distance = serializers.SerializerMethodField('get_distance')
    # addr = serializers.SerializerMethodField('get_old_address')

    class Meta:
        model = Store
        fields = ('id', 'name', 'category', 'description', 'lon', 'lat', 'thumbnail', 'contact',
                  'road_addr', 'common_addr', 'addr', 'tags', 'price_avg', 'partner', 'review_cnt', 'view_cnt',
                  'options', 'distance')

    def get_distance(self, obj):
        return int(obj.distance.m)

    def get_old_address(self, obj):
        return f'{obj.common_addr} {obj.addr}'


class ClientReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientReview
        fields = ('content',)

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



class StoreSearchSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    options = serializers.StringRelatedField(many=True)

    class Meta:
        model = Store
        fields = '__all__'