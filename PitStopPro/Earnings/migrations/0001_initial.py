# Generated by Django 4.2.11 on 2024-04-23 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                ("date", models.DateField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField()),
            ],
        ),
    ]
