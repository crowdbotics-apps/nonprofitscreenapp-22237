# Generated by Django 2.2.17 on 2020-11-02 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("call", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="phone",
            name="placecall",
        ),
    ]
