# Generated by Django 2.2.3 on 2019-08-09 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmster_server', '0012_auto_20190806_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
        migrations.AddField(
            model_name='agent',
            name='first_name',
            field=models.CharField(default='Chnir', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='last_name',
            field=models.CharField(default='Chnirovich', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
