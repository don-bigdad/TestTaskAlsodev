# Generated by Django 4.1 on 2022-11-07 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productcatalog', '0006_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]