# Generated by Django 5.0.2 on 2024-03-28 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("regions", "0001_initial"),
        ("shelterdb", "0003_alter_shelter_address_alter_shelter_facility_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="shelter",
            name="sido_code",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="regions.areasido",
            ),
            preserve_default=False,
        ),
    ]
