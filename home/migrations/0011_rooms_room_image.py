# Generated by Django 4.1.2 on 2022-10-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0010_remove_rooms_room_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="rooms",
            name="room_image",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]