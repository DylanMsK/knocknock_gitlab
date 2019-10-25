from rest_framework import serializers
from partners.models import BusinessRegistration
from accounts.models import Partner
from stores.models import Store
from stores.serializers import CategorySerializer, OptionSerializer


class PartnerStoresSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    options = OptionSerializer(many=True)

    class Meta:
        model = Store
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessRegistration
        fields = "__all__"
    
    def create(self, validated_data):
        partner = Partner.objects.get(pk=validated_data['partner_id'])
        store = Store.objects.get(pk=validated_data['store_id'])
        # registration = BusinessRegistration.objects.create(

        # )
        return partner