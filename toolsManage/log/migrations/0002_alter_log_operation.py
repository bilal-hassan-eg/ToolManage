# Generated by Django 4.2.2 on 2023-08-02 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='operation',
            field=models.CharField(choices=[('اضافة', 'اضافة'), ('سحب', 'سحب'), ('نقل', 'نقل')], default='اضافة', max_length=100),
        ),
    ]
