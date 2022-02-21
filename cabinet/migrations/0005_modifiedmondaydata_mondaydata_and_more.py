# Generated by Django 4.0.2 on 2022-02-20 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0004_alter_modified_data_monday_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModifiedMondayData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('subtasks', models.TextField()),
                ('contributor', models.TextField()),
                ('status', models.TextField()),
                ('timing', models.TextField()),
                ('ref', models.TextField()),
                ('workstatus', models.BooleanField(db_column='workStatus')),
            ],
            options={
                'db_table': 'modified_monday_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MondayData',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('subtasks', models.TextField()),
                ('contributor', models.TextField()),
                ('people', models.TextField()),
                ('status', models.TextField()),
                ('timing', models.TextField()),
            ],
            options={
                'db_table': 'monday_data',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='modified_Data_Monday',
        ),
        migrations.DeleteModel(
            name='monday_data',
        ),
    ]