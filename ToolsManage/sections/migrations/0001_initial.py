# Generated by Django 4.1.3 on 2022-12-24 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('notes', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('mac', models.CharField(max_length=100, null=True)),
                ('ip', models.CharField(max_length=100, null=True)),
                ('ssid', models.CharField(max_length=100, null=True)),
                ('model', models.CharField(max_length=100, null=True)),
                ('inventoryID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sections.inventory')),
                ('movementID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sections.movement')),
            ],
        ),
        migrations.AddField(
            model_name='movement',
            name='typeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sections.type'),
        ),
    ]
