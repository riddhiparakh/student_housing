# Generated by Django 4.1.2 on 2022-10-20 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0012_alter_rooms_room_image"),
    ]

    operations = [
        migrations.RemoveField(model_name="rooms", name="room_image",),
        migrations.AddField(
            model_name="rooms",
            name="room_image1",
            field=models.ImageField(null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="rooms",
            name="room_image2",
            field=models.ImageField(null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="rooms",
            name="room_image3",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
