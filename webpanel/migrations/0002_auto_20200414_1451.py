# Generated by Django 3.0.5 on 2020-04-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='Path',
            field=models.CharField(max_length=200),
        ),
    ]
