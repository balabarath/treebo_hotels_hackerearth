from hotel.models import deals, stats
from rest_framework import serializers

class DealsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = deals
        fields = ('id', 'name', 'image', 'rating', 'link', 'actual_price', 'discount', 'location')
        
class StatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = stats
        fields = ('api_hits')


