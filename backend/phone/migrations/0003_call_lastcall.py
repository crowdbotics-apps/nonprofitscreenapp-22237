# Generated by Django 2.2.17 on 2020-11-02 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0002_auto_20201102_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='lastcall',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]