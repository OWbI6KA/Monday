# Generated by Django 4.0.1 on 2022-02-14 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0003_modified_data_monday'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='modified_data_monday',
            table='modified_monday_data',
        ),
    ]