from rest_framework import serializers

from stores.models import Category, Store


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Store
        fields = '__all__'
