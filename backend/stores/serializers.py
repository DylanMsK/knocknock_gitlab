from rest_framework import serializers

from accounts.models import Partner, Client
from accounts.serializers.client_serializers import ClientSerializer
from stores.models import Category, Option, Store
from clients.serializers import ReviewSerializer
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


class StoreListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Store
        fields = ('id', 'name', 'category', 'lon', 'lat', 'thumbnail', 'contact', 'road_addr',
                  'common_addr', 'addr', 'view_cnt',)


class StoreDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    options = serializers.StringRelatedField(many=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    menus = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ('id', 'name', 'category', 'description', 'lon', 'lat', 'thumbnail', 'contact',
                  'road_addr', 'common_addr', 'addr', 'tags', 'price_avg', 'partner', 'review_cnt',
                  'view_cnt', 'menus', 'reviews', 'options')


