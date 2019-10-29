from rest_framework import serializers

from accounts.models import Partner, Client
from stores.models import Category, Option, Store, Review


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


class StoreReviewSerializer(serializers.ModelSerializer):
    store_id = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ('store_id', 'content')

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        print(user)
        client = Client.objects.get(user=user)
        print(client)
        store = Store.objects.get(pk=validated_data['store_id'])
        review = Review.objects.create(
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