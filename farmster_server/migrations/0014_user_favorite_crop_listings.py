# Generated by Django 2.2.3 on 2019-08-08 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmster_server', '0013_auto_20190806_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_crop_listings',
            field=models.ManyToManyField(related_name='users', to='farmster_server.CropListing'),
        ),
    ]
