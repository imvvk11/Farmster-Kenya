# Generated by Django 2.2.3 on 2019-08-06 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmster_server', '0011_auto_20190805_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='places',
            field=models.ManyToManyField(related_name='users', to='farmster_server.Place'),
        ),
        migrations.AlterField(
            model_name='user',
            name='crops',
            field=models.ManyToManyField(related_name='users', to='farmster_server.Crop'),
        ),
        migrations.AlterField(
            model_name='user',
            name='default_place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_id', to='farmster_server.Place'),
        ),
    ]