# Generated by Django 2.2.3 on 2019-08-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmster_server', '0016_auto_20190811_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255, unique=True)),
                ('places', models.ManyToManyField(related_name='farmers', to='farmster_server.Place')),
            ],
        ),
    ]
