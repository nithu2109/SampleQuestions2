# Generated by Django 3.2.9 on 2022-02-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bustickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bus_No', models.IntegerField()),
                ('Destinations', models.CharField(max_length=50)),
                ('No_of_Persons', models.IntegerField()),
            ],
        ),
    ]