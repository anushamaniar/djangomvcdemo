# Generated by Django 4.2.5 on 2023-10-06 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("std", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="division",
            field=models.CharField(default="CE", max_length=10),
        ),
    ]
