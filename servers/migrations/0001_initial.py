# Generated by Django 3.0.5 on 2020-04-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('IP', models.GenericIPAddressField()),
                ('Port', models.IntegerField()),
                ('Path', models.CharField(max_length=200)),
            ],
        ),
    ]
