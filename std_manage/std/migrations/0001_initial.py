# Generated by Django 4.2.5 on 2023-09-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("roll", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=10)),
                ("address", models.CharField(max_length=200)),
            ],
        ),
    ]