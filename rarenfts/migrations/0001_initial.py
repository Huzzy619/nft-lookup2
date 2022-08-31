# Generated by Django 4.1 on 2022-08-31 15:56

from django.db import migrations, models
import django.db.models.deletion
import rarenfts.helpers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Collection",
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
                ("name", models.CharField(max_length=255)),
                (
                    "guid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "network",
                    models.CharField(
                        choices=[
                            ("Null", "Null"),
                            ("SOL", "SOLANA"),
                            ("ETH", "ETHEREUM"),
                            ("BSC", "BSC"),
                            ("MATIC", "MATIC"),
                        ],
                        default="ETH",
                        max_length=255,
                    ),
                ),
                (
                    "floor_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0, max_digits=6, null=True
                    ),
                ),
                (
                    "volume",
                    models.PositiveIntegerField(blank=True, default=0, null=True),
                ),
                ("date", models.DateField()),
                ("discord", models.URLField(blank=True, max_length=550, null=True)),
                ("twitter", models.URLField(blank=True, max_length=550, null=True)),
                ("website", models.URLField(blank=True, max_length=550, null=True)),
                (
                    "listing_type",
                    models.CharField(
                        choices=[("free", "free"), ("paid", "paid")],
                        default="free",
                        max_length=10,
                    ),
                ),
                (
                    "verification",
                    models.BooleanField(
                        default=False,
                        help_text="Only approved collections will be visible on the list page",
                        verbose_name="approve",
                    ),
                ),
                (
                    "featured",
                    models.BooleanField(
                        default=False,
                        help_text="Toggle this option to make a collection display as featured",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
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
                ("link", models.URLField(max_length=550)),
                (
                    "collection",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transaction_link",
                        to="rarenfts.collection",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NFT",
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
                    "image",
                    models.ImageField(upload_to=rarenfts.helpers.get_media_paths),
                ),
                (
                    "collection",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="rarenfts.collection",
                    ),
                ),
            ],
        ),
    ]
