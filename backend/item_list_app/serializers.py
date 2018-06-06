from rest_framework import serializers
from item_list_app.models import Card
from item_list_app.models import otherItem


class CardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Card
		fields = ('id','cardNo','foundTime','keep','status','phone')

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = otherItem
		fields = ('id','itemName','foundTime','keep','status','phone','description')