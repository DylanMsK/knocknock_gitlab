from rest_framework import serializers

from accounts.models import Partner
from stores.models import Category, Option, Store


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

    class Meta:
        model = Store
        fields = '__all__'
