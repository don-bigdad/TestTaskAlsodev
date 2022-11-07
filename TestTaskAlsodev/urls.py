"""TestTaskAlsodev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from productcatalog.views import Catalog, ProductUpdate, ProductDetail, DeleteProduct, product_append

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("frontend.urls")),
    path("catalog/",Catalog.as_view(),name="Catalog"),
    path("delete/",DeleteProduct.as_view(),name="Delete"),
    path("append/",product_append,name="append"),
    path("update/<int:pk>/", ProductUpdate.as_view(),name="Product_Update"),
    path("detail/<int:pk>/", ProductDetail.as_view()),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)