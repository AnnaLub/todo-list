# Generated by Django 5.2.1 on 2025-05-21 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["done", "-created_time"]},
        ),
    ]
