# Generated by Django 2.2.3 on 2019-10-06 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmster_server', '0032_auto_20190922_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='croplisting',
            options={'ordering': ('harvest_date',)},
        ),
    ]
