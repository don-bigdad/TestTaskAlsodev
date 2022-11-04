from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    picture1 = models.ImageField(upload_to="product/%Y-%m-%d")
    picture2 = models.ImageField(blank=True,upload_to="product/%Y-%m-%d")
    author = models.CharField(max_length=50)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.author}'
