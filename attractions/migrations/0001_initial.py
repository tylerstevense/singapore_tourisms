# Generated by Django 4.1.2 on 2022-11-01 13:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attraction",
            fields=[
                (
                    "uuid",
                    models.TextField(primary_key=True, serialize=False, unique=True),
                ),
                ("name", models.CharField(max_length=300)),
                (
                    "attraction_type",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                ("summary", models.TextField(blank=True, null=True)),
                ("is_full_record", models.BooleanField(default=False)),
                ("full_description", models.TextField(blank=True, null=True)),
                ("nearest_station", models.TextField(blank=True, null=True)),
                (
                    "website_url",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                ("admission_info", models.TextField(blank=True, null=True)),
                ("map_url", models.URLField(blank=True, null=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("content", models.TextField(blank=True, verbose_name="Comment")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Outing",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("start_time", models.DateTimeField()),
                ("start_notification_sent", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ["-start_time"],
            },
        ),
        migrations.CreateModel(
            name="OutingInvitation",
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
                ("attendance_confirmed", models.BooleanField(default=False)),
                ("is_attending", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="SearchTerm",
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
                ("term", models.TextField(unique=True)),
                ("last_search_date", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["last_search_date"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=300)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]
