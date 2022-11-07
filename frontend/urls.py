from django.contrib import admin
from django.urls import path, include

from frontend.views import catalog
from productcatalog.views import Catalog, ProductDetail

urlpatterns = [

    path("",catalog,name="catalog"),
]
