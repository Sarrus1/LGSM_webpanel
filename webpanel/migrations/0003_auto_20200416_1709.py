# Generated by Django 3.0.5 on 2020-04-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpanel', '0002_auto_20200414_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='IP',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='server',
            name='Port',
            field=models.IntegerField(),
        ),
    ]
