# Generated by Django 4.1.3 on 2022-11-04 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('picture1', models.ImageField(upload_to='product/%Y-%m-%d')),
                ('picture2', models.ImageField(blank=True, upload_to='product/%Y-%m-%d')),
                ('author', models.CharField(max_length=50)),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
