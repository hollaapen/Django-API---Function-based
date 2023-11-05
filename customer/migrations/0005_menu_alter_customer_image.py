# Generated by Django 4.2.3 on 2023-10-15 18:06

import customer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_customer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='logo.png', upload_to=customer.models.upload_path),
        ),
    ]
