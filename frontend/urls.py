from django.contrib import admin
from django.urls import path, include

from frontend.views import catalog

urlpatterns = [
    path("",catalog,name="Catalog"),
]
