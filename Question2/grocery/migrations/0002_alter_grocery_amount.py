# Generated by Django 3.2.9 on 2022-02-13 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]