# Generated by Django 2.2.3 on 2019-08-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmster_server', '0007_auto_20190804_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='crops',
            field=models.ManyToManyField(null=True, to='farmster_server.Crop'),
        ),
    ]