from rest_framework import serializers
from accounts.models import Partner
from stores.models import Store

class PartnerStoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'