# Generated by Django 3.0.5 on 2020-04-14 14:28

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
                ('IP', models.CharField(max_length=15)),
                ('Port', models.CharField(max_length=5)),
                ('Path', models.TextField()),
            ],
        ),
    ]