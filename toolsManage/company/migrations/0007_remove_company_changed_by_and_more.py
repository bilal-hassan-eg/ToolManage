# Generated by Django 4.1.3 on 2023-03-17 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_company_changed_by_historicalcompany_changed_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='historicalcompany',
            name='changed_by',
        ),
    ]