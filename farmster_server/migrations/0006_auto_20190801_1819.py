# Generated by Django 2.2.3 on 2019-08-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmster_server', '0005_auto_20190801_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]