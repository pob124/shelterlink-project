# Generated by Django 5.0.2 on 2024-03-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shelterdb", "0002_alter_shelter_area"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shelter",
            name="address",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="shelter",
            name="facility_name",
            field=models.CharField(max_length=30),
        ),
    ]
