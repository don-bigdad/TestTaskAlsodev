# Generated by Django 4.1 on 2022-11-07 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productcatalog', '0005_alter_product_author_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, upload_to='product/%Y-%m-%d'),
        ),
    ]
