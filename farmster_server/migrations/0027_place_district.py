# Generated by Django 2.2.3 on 2019-08-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmster_server', '0026_dealpart_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='district',
            field=models.CharField(default='Natanya District', max_length=255),
            preserve_default=False,
        ),
    ]
