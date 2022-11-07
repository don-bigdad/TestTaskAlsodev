
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *

from .serializers import ProductSerializer


class ProductUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DeleteProduct(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class ProductAppend(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class Catalog(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['POST'])
def product_append(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(Catalog)