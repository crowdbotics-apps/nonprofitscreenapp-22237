# Generated by Django 2.2.17 on 2020-11-02 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("phone", "0001_initial"),
        ("call", "0002_remove_phone_placecall"),
    ]

    operations = [
        migrations.AddField(
            model_name="phone",
            name="call",
            field=models.ManyToManyField(
                blank=True, related_name="phone_call", to="phone.Call"
            ),
        ),
    ]
