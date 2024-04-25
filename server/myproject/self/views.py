from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from self.models import Items
from self.serializers import ItemsSerializer
from rest_framework import status
from rest_framework import serializers
# Create your views here.

@api_view(['GET'])
def view_items(request):
    print('-----------',request.query_params)
    if request.query_params:
        items=Items.objects.filter(**request.query_params.dict())
    else:
        items=Items.object.all()

    if items:
        serializer=ItemsSerializer(items,many=True)
        return Response({"data":serializer.data})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)






@api_view(['POST'])
def add_items(request):
    print(request.data)
    item1 = ItemsSerializer(data=request.data)
    if Items.objects.filter(**request.data).exists():
        print('exist')
        # raise serializers.validationError('already exist')
        return Response({"values":'already exist'})
    
    if item1.is_valid():
        item1.save()
        return Response({"values":item1.data})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# {"name":"car","rate":12}