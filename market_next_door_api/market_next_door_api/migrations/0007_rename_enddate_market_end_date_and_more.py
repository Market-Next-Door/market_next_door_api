# Generated by Django 4.2.7 on 2023-12-03 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market_next_door_api', '0006_alter_vendor_market'),
    ]

    operations = [
        migrations.RenameField(
            model_name='market',
            old_name='enddate',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='market',
            old_name='startdate',
            new_name='start_date',
        ),
    ]
