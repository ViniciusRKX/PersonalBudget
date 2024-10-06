# Generated by Django 5.1 on 2024-09-14 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personalbudgets", "0002_personalbudget_delete_personalbudgets"),
    ]

    operations = [
        migrations.RenameField(
            model_name="personalbudget",
            old_name="amount",
            new_name="total_amount",
        ),
        migrations.RemoveField(
            model_name="personalbudget",
            name="spent",
        ),
        migrations.AddField(
            model_name="personalbudget",
            name="remaining_amount",
            field=models.DecimalField(
                decimal_places=2, default=0, editable=False, max_digits=10
            ),
            preserve_default=False,
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateField(auto_now_add=True)),
                ("notes", models.TextField(blank=True)),
                (
                    "budget",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="personalbudgets.personalbudget",
                    ),
                ),
            ],
        ),
    ]
