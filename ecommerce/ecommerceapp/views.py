from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializers import Tamazonserializer
from .models import Tamazon
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

# Create your views here.
# class Tamazonview(APIView):
#     #GET request to get all the items from the database
#     # def get(self,request):
#     #     all_products = Tamazon.objects.values()
#     #     list_of_items=[]
#     #     for product in all_products:
#     #         data={}
#     #         data['id']=product['id']
#     #         data['item_name']=product['item_name']
#     #         data['item_features']=product['item_features']
#     #         data['item_rating']=product['item_rating']
#     #         data['item_offers']=product['item_offers']
#     #         data['item_price']=product['item_price']
#     #         list_of_items.append(data)
#     #     if len(list_of_items)>0:
#     #         return Response({"message":list_of_items,'success':'true'},status=status.HTTP_200_OK)
#     #     else:
#     #         return Response({"message":'No items in the database','success':'false'},status=status.HTTP_404_NOT_FOUND)

#     # # POST request to create new item in the database
#     # # def post(self,request):
#     # #     serializer = Tamazonserializer(data=request.data)
#     # #     if serializer.is_valid():
#     # #         serializer.save()
#     # #         return Response({'message':'Item created','success':'true'},status=status.HTTP_201_CREATED)
#     # #     return Response({'message':serializer.errors,'success':'false'},status=status.HTTP_400_BAD_REQUEST)

#     # #PUT request to edit an existing item in the database
#     # def post(self,request):
#     #     item_name= request.POST['item_name']
#     #     item_features =request.data['item_features']
#     #     item_price =request.data['item_price']
#     #     item_offers =request.data['item_offers']
#     #     if Tamazon.objects.filter(item_name=item_name).exists():
#     #         item = Tamazon.objects.filter(item_name=item_name).last()
#     #         item.item_features = item_features
#     #         item.item_price = item_price
#     #         item.item_offers = item_offers
#     #         item.save()
#     #         return Response({'message':'Item updated','success':'true'},status=status.HTTP_202_ACCEPTED)
#     #     return Response({'message':'Could not find any such item','success':'false'},status=status.HTTP_400_BAD_REQUEST)

#     # #DELETE request to delete an item from the database
#     # def delete(self,request):
#     #     item_name = request.data['item_name']
#     #     if Tamazon.objects.filter(item_name=item_name).exists():
#     #         item = Tamazon.objects.filter(item_name=item_name).last()
#     #         item.delete()
#     #         return Response({'message':'Item deleted successfully','success':'true'},status=status.HTTP_200_OK)
#     #     return Response({'message':'Could not find any such item','success':'false'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'append_these_after_https://ezpz4me.pythonanywhere.com/':" to make the changes",
        'all_items': 'all/',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_items(request):
    serializer = Tamazonserializer(data=request.data)

    # validating for already existing data
    # if Tamazon.objects.filter(**request.data).exists():
    #     raise serializers.ValidationError('This data already exists')

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_items(request):

    # checking for the parameters from the URL
    # if request.query_params:
    #     items = Tamazon.objects.filter(**request.query_param.dict())
    # else:
    items = Tamazon.objects.values()

    # if there is something in items else raise error
    if items:
        # data = Tamazonserializer(items)
        # print(data)
        return Response(items)
    else:
        return Response("No data found",status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_items(request, pk):
    item = Tamazon.objects.get(pk=pk)
    data = Tamazonserializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response("Unable to update, couldn't find the id",status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Tamazon, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

