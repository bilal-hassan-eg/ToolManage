# Generated by Django 4.2.2 on 2023-07-28 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0012_remove_historicaltool_storeid_remove_tool_storeid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaltool',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='tool',
            name='quantity',
        ),
    ]