# Generated by Django 5.1.6 on 2025-02-27 04:55

import maruza1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                    "name",
                    models.CharField(max_length=255, verbose_name="Ism Familiyasi"),
                ),
                ("birth_year", models.IntegerField(verbose_name="Tug'ilgan yili")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Oliy", "Oliy"),
                            ("Birinchi", "Birinchi"),
                            ("Ikkinchi", "Ikkinchi"),
                        ],
                        max_length=50,
                        verbose_name="Toifasi",
                    ),
                ),
                (
                    "category_certificate",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=maruza1.models.unique_file_path,
                        verbose_name="Toifa sertifikati",
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        choices=[
                            ("math", "Matematika"),
                            ("physics", "Fizika"),
                            ("chemistry", "Himiya"),
                            ("biology", "Biologiya"),
                            ("history", "Tarix"),
                        ],
                        max_length=50,
                        verbose_name="Dars beradigan fani",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=maruza1.models.unique_file_path,
                        verbose_name="Rasm",
                    ),
                ),
                (
                    "additional_info",
                    models.TextField(blank=True, verbose_name="Qo'shimcha ma'lumotlar"),
                ),
            ],
        ),
    ]
