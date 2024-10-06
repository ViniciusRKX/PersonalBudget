# Generated by Django 5.1 on 2024-10-05 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personalbudgets", "0017_alter_personalbudget_remaining_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalbudget",
            name="remaining_amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
