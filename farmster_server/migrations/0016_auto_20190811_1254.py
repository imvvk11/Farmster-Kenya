# Generated by Django 2.2.3 on 2019-08-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmster_server', '0015_merge_20190811_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='name_sw',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='name_sw',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
