from rest_framework import serializers
from .models import *

class SuvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suv
        fields = '__all__'

class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'

class HaydovchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = '__all__'

class HaydovchiDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'ism', 'tel_raqam', 'smena')

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'
        extra_kwargs = {
            'admin': {'read_only': True},
        }