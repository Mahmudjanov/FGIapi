from rest_framework import serializers
from.models import *


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"



class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = "__all__"