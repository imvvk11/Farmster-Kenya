# Generated by Django 2.2.3 on 2019-10-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmster_server', '0038_auto_20191030_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='agents',
            field=models.ManyToManyField(blank=True, related_name='places', to='farmster_server.Agent'),
        ),
    ]
