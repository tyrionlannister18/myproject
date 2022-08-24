# Generated by Django 4.0.5 on 2022-08-15 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('did', models.IntegerField(primary_key=True, serialize=False)),
                ('manufacture', models.CharField(max_length=10)),
                ('freq', models.IntegerField()),
                ('model', models.CharField(max_length=20)),
            ],
        ),
    ]
