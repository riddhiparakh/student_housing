# Generated by Django 4.1.2 on 2022-10-16 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_capacity_food_room_type_delete_host_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="User",),
    ]
