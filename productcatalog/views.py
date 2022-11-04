
from rest_framework import generics


from .models import *

from .serializers import ProductSerializer


class catalog(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer