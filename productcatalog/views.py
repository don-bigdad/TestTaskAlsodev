
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *

from .serializers import ProductSerializer





class Catalog(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['POST'])
def product_update(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def product_append(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(Catalog)


@api_view(['DELETE'])
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('Item succsesfully delete!')