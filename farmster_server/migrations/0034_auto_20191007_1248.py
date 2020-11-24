# Generated by Django 2.2.3 on 2019-10-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmster_server', '0033_auto_20191006_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='croplisting',
            name='amount_unit',
            field=models.CharField(choices=[('KGS', 'KGS'), ('TONS', 'TONS'), ('BOXES', 'BOXES'), ('TRUCKS', 'TRUCKS'), ('PIECES', 'PIECES'), ('BAGS', 'BAGS'), ('CRATES', 'CRATES'), ('L', 'L'), ('SACKS', 'SACKS'), ('BUNDLES', 'BUNDLES'), ('TREES', 'TREES'), ('TINS', 'TINS'), ('OTHER', 'OTHER')], default='KGS', max_length=255),
        ),
        migrations.AlterField(
            model_name='dealpart',
            name='amount_unit',
            field=models.CharField(choices=[('KGS', 'KGS'), ('TONS', 'TONS'), ('BOXES', 'BOXES'), ('TRUCKS', 'TRUCKS'), ('PIECES', 'PIECES'), ('BAGS', 'BAGS'), ('CRATES', 'CRATES'), ('L', 'L'), ('SACKS', 'SACKS'), ('BUNDLES', 'BUNDLES'), ('TREES', 'TREES'), ('TINS', 'TINS'), ('OTHER', 'OTHER')], default='KGS', max_length=255),
        ),
    ]
