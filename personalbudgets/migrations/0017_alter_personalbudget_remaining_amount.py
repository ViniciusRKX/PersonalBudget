# Generated by Django 5.1 on 2024-10-05 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personalbudgets", "0016_alter_personalbudget_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalbudget",
            name="remaining_amount",
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10),
        ),
    ]
