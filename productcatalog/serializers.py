from rest_framework import serializers

from productcatalog.views import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name","price","picture1","picture2","author","date_of_creation",)