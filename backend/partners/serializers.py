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
    store_id = serializers.IntegerField()
    # registration_image = serializers.ImageField()

    class Meta:
        model = BusinessRegistration
        fields = ('store_id', 'company_name', 'business_registration_number',
                  'representative_name', 'business_address')

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            if user is None:
                raise serializers.ValidationError("존재하지 않는 User입니다.")
        partner = Partner.objects.get(user=user)
        store = Store.objects.get(pk=validated_data['store_id'])
        store.partner = partner
        store.save()
        
        registration = BusinessRegistration.objects.create(
            store=store,
            partner=partner,
            company_name=validated_data['company_name'],
            business_registration_number=validated_data['business_registration_number'],
            representative_name=validated_data['representative_name'],
            business_address=validated_data['business_address'],
            # registration_image=validated_data['registration_image']
        )
        return registration