from dataclasses import fields
from rest_framework import serializers
from .models import Tamazon


class Tamazonserializer(serializers.ModelSerializer):
    class Meta():
        model=Tamazon
        fields=("item_name","item_rating","item_price","item_offers","item_features")
