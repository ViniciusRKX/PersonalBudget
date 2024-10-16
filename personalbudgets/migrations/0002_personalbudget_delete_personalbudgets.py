# Generated by Django 5.1 on 2024-09-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personalbudgets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PersonalBudget",
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
                ("spent", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateField(auto_now_add=True)),
                ("category", models.CharField(blank=True, max_length=100)),
                ("notes", models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name="PersonalBudgets",
        ),
    ]
