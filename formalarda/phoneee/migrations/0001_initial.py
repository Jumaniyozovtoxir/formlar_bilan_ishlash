# Generated by Django 4.0.1 on 2022-01-16 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telefon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=700)),
                ('nomi', models.CharField(max_length=700)),
                ('xotira', models.IntegerField()),
                ('rangi', models.CharField(max_length=70)),
                ('narxi', models.CharField(max_length=70)),
            ],
        ),
    ]