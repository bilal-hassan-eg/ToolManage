# Generated by Django 4.2.2 on 2023-07-28 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_historicalstore_location_alter_store_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalstore',
            name='RealNumberTools',
        ),
        migrations.RemoveField(
            model_name='store',
            name='RealNumberTools',
        ),
    ]
