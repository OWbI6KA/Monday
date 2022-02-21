# Generated by Django 4.0.1 on 2022-02-21 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0005_modifiedmondaydata_mondaydata_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainData',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('subtasks', models.TextField()),
                ('contributor', models.TextField()),
                ('people', models.TextField()),
                ('status', models.BooleanField()),
                ('timing', models.DateTimeField()),
                ('textWorker', models.TextField()),
                ('photoWorker', models.ImageField(upload_to='')),
                ('doneByWorker', models.BooleanField()),
                ('doneByLeader', models.BooleanField()),
            ],
            options={
                'db_table': 'main_data',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='modifiedmondaydata',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='mondaydata',
            options={'managed': True},
        ),
    ]