# Generated by Django 4.2.7 on 2023-12-05 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_next_door_api', '0011_remove_preorder_item_preorder_items_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='preorder',
            name='quantity_of_item',
            field=models.IntegerField(default=1),
        ),
    ]
