from rest_framework import serializers

from stores.models import Store
from menus.models import Menu


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'

    def create(self, validated_data):
        store_id = self.context.get('view').kwargs.get('store_id')
        if store_id is None:
            raise serializers.ValidationError("해당 Store가 존재하지 않습니다.")
        store = Store.objects.get(pk=store_id)

        menu = Menu.objects.create(
            store=store,
            name=validated_data['name'],
            thumbnail=validated_data['thumbnail'],
            price=validated_data['price'],
            description=validated_data['description']
        )
        return menu