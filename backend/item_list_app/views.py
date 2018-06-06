from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from item_list_app.models import Card
from item_list_app.serializers import CardSerializer
from item_list_app.models import otherItem
from item_list_app.serializers import ItemSerializer
from django.db.models import Q

headers = {
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
    "Access-Control-Allow-Origin": "*"
}

@api_view(['GET','POST'])
def card_list(request,format=None):
	if request.method == 'GET':
		cards=Card.objects.all()
		serializer=CardSerializer(cards,many=True)
		return Response(serializer.data,headers=headers)
	elif request.method == 'POST':
		serializer=CardSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,headers=headers)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,headers=headers)

@api_view(['GET', 'PUT', 'DELETE'])
def card_detail(request,pk,format=None):
	try:
		card=Card.objects.filter(cardNo__icontains=pk)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND,headers=headers)

	if request.method == 'GET':
		serializer=CardSerializer(card,many=True)
		return Response(serializer.data,headers=headers)
	elif request.method == 'PUT':
		serializer=CardSerializer(card,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.dat,headers=headers)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,headers=headers)
	elif request.method == 'DELETE':
		card.delete()
		return Response(status=status.HTTP_204_NO_CONTENT,headers=headers)

@api_view(['GET','POST'])
def item_list(request,format=None):
	if request.method == 'GET':
		items=otherItem.objects.all()
		serializer=ItemSerializer(items,many=True)
		return Response(serializer.data,headers=headers)
	elif request.method == 'POST':
		serializer=ItemSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,headers=headers)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,headers=headers)

@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request,pk,format=None):
	try:
		item=otherItem.objects.get(id=pk)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND,headers=headers)

	if request.method == 'GET':
		serializer=ItemSerializer(item)
		return Response(serializer.data,headers=headers)
	elif request.method == 'PUT':
		serializer=ItemSerializer(item,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.dat,headers=headers)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,headers=headers)
	elif request.method == 'DELETE':
		item.delete()
		return Response(status=status.HTTP_204_NO_CONTENT,headers=headers)


@api_view(['GET'])
def search_item(request,pk,format=None):
	items=otherItem.objects.filter(Q(itemName__icontains = pk)|Q(description__icontains = pk))

	if request.method == 'GET':
		serializer=ItemSerializer(items,many=True)
		return Response(serializer.data,headers=headers)

