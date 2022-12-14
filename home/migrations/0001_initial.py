# Generated by Django 4.1.2 on 2022-10-10 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Host",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("phone", models.IntegerField()),
                ("email", models.CharField(blank=True, max_length=100, null=True)),
                ("address", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Preferences",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "room",
                    models.CharField(
                        choices=[
                            ("Shared room", "Shared room"),
                            ("pvt room", "Private room"),
                        ],
                        default="shared room",
                        max_length=50,
                    ),
                ),
                (
                    "roommate_no",
                    models.IntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1
                    ),
                ),
                (
                    "preferred_cusine",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("veg", "Vegetarian"),
                            ("non-veg", "Non-vegetarian"),
                            ("none", "none"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "eminity1",
                    models.CharField(
                        choices=[
                            ("Common TV room", "Common TV room"),
                            ("common reading room", "Common reading room"),
                            ("Dining Facilities", "Dining Facilities"),
                            ("Free wifi", "Free Wifi"),
                            ("gym", "Gym"),
                            ("house help", "House help"),
                            ("washing machine", "Washing Machine"),
                            ("electricity", "Electricity"),
                            ("gas", "Gas"),
                            ("24-hour running water", "24-hour running water"),
                            (
                                "only few hours runnimg water",
                                "Only few hours running water",
                            ),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "eminity2",
                    models.CharField(
                        choices=[
                            ("Common TV room", "Common TV room"),
                            ("common reading room", "Common reading room"),
                            ("Dining Facilities", "Dining Facilities"),
                            ("Free wifi", "Free Wifi"),
                            ("gym", "Gym"),
                            ("house help", "House help"),
                            ("washing machine", "Washing Machine"),
                            ("electricity", "Electricity"),
                            ("gas", "Gas"),
                            ("24-hour running water", "24-hour running water"),
                            (
                                "only few hours runnimg water",
                                "Only few hours running water",
                            ),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "eminity3",
                    models.CharField(
                        choices=[
                            ("Common TV room", "Common TV room"),
                            ("common reading room", "Common reading room"),
                            ("Dining Facilities", "Dining Facilities"),
                            ("Free wifi", "Free Wifi"),
                            ("gym", "Gym"),
                            ("house help", "House help"),
                            ("washing machine", "Washing Machine"),
                            ("electricity", "Electricity"),
                            ("gas", "Gas"),
                            ("24-hour running water", "24-hour running water"),
                            (
                                "only few hours runnimg water",
                                "Only few hours running water",
                            ),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "eminity4",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Common TV room", "Common TV room"),
                            ("common reading room", "Common reading room"),
                            ("Dining Facilities", "Dining Facilities"),
                            ("Free wifi", "Free Wifi"),
                            ("gym", "Gym"),
                            ("house help", "House help"),
                            ("washing machine", "Washing Machine"),
                            ("electricity", "Electricity"),
                            ("gas", "Gas"),
                            ("24-hour running water", "24-hour running water"),
                            (
                                "only few hours runnimg water",
                                "Only few hours running water",
                            ),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "eminity5",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Common TV room", "Common TV room"),
                            ("common reading room", "Common reading room"),
                            ("Dining Facilities", "Dining Facilities"),
                            ("Free wifi", "Free Wifi"),
                            ("gym", "Gym"),
                            ("house help", "House help"),
                            ("washing machine", "Washing Machine"),
                            ("electricity", "Electricity"),
                            ("gas", "Gas"),
                            ("24-hour running water", "24-hour running water"),
                            (
                                "only few hours runnimg water",
                                "Only few hours running water",
                            ),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "eminity6",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Common TV room", "Common TV room"),
                            ("common reading room", "Common reading room"),
                            ("Dining Facilities", "Dining Facilities"),
                            ("Free wifi", "Free Wifi"),
                            ("gym", "Gym"),
                            ("house help", "House help"),
                            ("washing machine", "Washing Machine"),
                            ("electricity", "Electricity"),
                            ("gas", "Gas"),
                            ("24-hour running water", "24-hour running water"),
                            (
                                "only few hours runnimg water",
                                "Only few hours running water",
                            ),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "eminity7",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Common TV room", "Common TV room"),
                            ("common reading room", "Common reading room"),
                            ("Dining Facilities", "Dining Facilities"),
                            ("Free wifi", "Free Wifi"),
                            ("gym", "Gym"),
                            ("house help", "House help"),
                            ("washing machine", "Washing Machine"),
                            ("electricity", "Electricity"),
                            ("gas", "Gas"),
                            ("24-hour running water", "24-hour running water"),
                            (
                                "only few hours runnimg water",
                                "Only few hours running water",
                            ),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"verbose_name_plural": "Preference",},
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("phone", models.IntegerField()),
                ("email", models.CharField(blank=True, max_length=100, null=True)),
                ("address", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"verbose_name_plural": "User",},
        ),
        migrations.CreateModel(
            name="Rooms",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("building_name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=500)),
                (
                    "preference_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.preferences",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Rooms",},
        ),
    ]
