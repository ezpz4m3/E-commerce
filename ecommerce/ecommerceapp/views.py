from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializers import Tamazonserializer
from .models import Tamazon

# Create your views here.

class Tamazonview(APIView):

    #GET request to get all the items from the database
    def get(self,request):
        all_products = Tamazon.objects.values()
        list_of_items=[]
        for product in all_products:
            data={}
            data['id']=product['id']
            data['item_name']=product['item_name']
            data['item_features']=product['item_features'] 
            data['item_rating']=product['item_rating']
            data['item_offers']=product['item_offers']
            data['item_price']=product['item_price']  
            list_of_items.append(data) 
        if len(list_of_items)>0:
            return Response({"message":list_of_items,'success':'true'},status=status.HTTP_200_OK)
        else:
            return Response({"message":'No items in the database','success':'false'},status=status.HTTP_404_NOT_FOUND)

    #POST request to create new item in the database
    def post(self,request):
        serializer = Tamazonserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Item created','success':'true'},status=status.HTTP_201_CREATED)
        return Response({'message':serializer.errors,'success':'false'},status=status.HTTP_400_BAD_REQUEST)

    #PUT request to edit an existing item in the database
    def put(self,request):
        item_name= request.data['item_name']
        item_features =request.data['item_features']
        item_price =request.data['item_price']
        item_offers =request.data['item_offers']
        if Tamazon.objects.filter(item_name=item_name).exists():
            item = Tamazon.objects.filter(item_name=item_name).last()
            item.item_features = item_features
            item.item_price = item_price
            item.item_offers = item_offers
            item.save()
            return Response({'message':'Item updated','success':'true'},status=status.HTTP_202_ACCEPTED)
        return Response({'message':'Could not find any such item','success':'false'},status=status.HTTP_400_BAD_REQUEST)

    #DELETE request to delete an item from the database
    def delete(self,request):
        item_name = request.data['item_name']
        if Tamazon.objects.filter(item_name=item_name).exists():
            item = Tamazon.objects.filter(item_name=item_name).last()
            item.delete()
            return Response({'message':'Item deleted successfully','success':'true'},status=status.HTTP_200_OK)
        return Response({'message':'Could not find any such item','success':'false'},status=status.HTTP_400_BAD_REQUEST)
