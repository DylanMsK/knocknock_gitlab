from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
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


class RegisterBusinessRegistration(serializers.ModelSerializer):
    store_id = serializers.CharField(max_length=10)
    registration_image = serializers.ImageField()

    class Meta:
        model = BusinessRegistration
        fields = ('store_id', 'is_new', 'company_name', 'business_registration_number',
                  'representative_name', 'business_address', 'registration_image')
    
    def create(self, validated_data):
        partner = Partner.objects.get(user=CurrentUserDefault())
        store = Store.objects.get(pk=validated_data['store_id'])
        registration = BusinessRegistration.objects.create(
            store=store,
            partner=partner,
            is_new=validated_data['is_new'],
            company_name=validated_data['company_name'],
            business_registration_number=validated_data['business_registration_number'],
            representative_name=validated_data['representative_name'],
            business_address=validated_data['business_address'],
            registration_image=validated_data['registration_image']
        )
        return registration