# Generated by Django 4.2.2 on 2023-07-10 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("PM_APP", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="proyect",
            new_name="project",
        ),
    ]