# Generated by Django 5.1 on 2024-09-14 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "personalbudgets",
            "0004_remove_personalbudget_category_transaction_category_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="transaction",
            old_name="amount",
            new_name="price",
        ),
    ]
